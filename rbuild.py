""" Project build script.

This will build/install the project's C++ binaries using CMake. The script can
either be run directly on the target machine or remotely using Vagrant or SSH.

The `--config` option must be used the first time the project is built. If
`--build` and `--install` are both specified, they should refer to the same
build type or `--install` will have no effect.

For Vagrant builds, the VM will be started if it is not already running.


CLion and Vagrant
-----------------

Use this to create a local Python configuration for building on a Vagrant VM.
That configuration can then be used as a 'Before launch' tool for other
configurations, e.g. for ensuring that executables are always up-to-date
before running a test suite.

"""
from argparse import ArgumentParser
from errno import EEXIST
from errno import ENOENT
from os import makedirs
from os import chdir
from os.path import abspath
from os.path import join
from shlex import split
from shutil import rmtree
from subprocess import call
from subprocess import check_call
from subprocess import check_output


_BUILDS = "Debug", "Release"


def main(argv=None):
    """ Script execution.

    """
    def config():
        """ Run the CMake config step for the current build. """
        try:
            # Make the build directory if it does not exist.
            makedirs(path)
        except OSError as err:
            if err.errno != EEXIST:
                raise  # unexpected error
        chdir(path)
        cmake = "cmake -DCMAKE_BUILD_TYPE={:s} {:s}".format(build, args.root)
        check_call(split(cmake))
        return

    args = _args(argv)
    if args.ssh or args.vagrant:
        return _remote(args)
    args.root = abspath(args.root)
    builds = [args.build.title()] if args.build else _BUILDS
    for build in builds:
        path = join(args.root, "build", build)
        if args.clean:
            # This is a hard clean that removes all CMake artifacts as well as
            # binaries, so the config step needs to be run again.
            try:
                rmtree(path)
            except OSError as err:
                if err.errno != ENOENT:
                    raise  # unexpected error
            args.config = True
        if args.config:
            config()
        cmake = "cmake --build {:s}".format(path)
        check_call(split(cmake))
    return 0


def _args(argv=None):
    """ Parse command line arguments.

    By default, sys.argv is parsed.

    """
    # The -h/--help option is defined automatically by argparse.
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", action="store_true",
            help="run CMake config first [False]")
    parser.add_argument("-C", "--clean", action="store_true",
            help="clean before building (implies --config) [False]")
    parser.add_argument("-b", "--build", help="build type [all]")
    remote = parser.add_mutually_exclusive_group()
    remote.add_argument("-V", "--vagrant", help="connect to Vagrant VM box")
    remote.add_argument("-S", "--ssh", help="connect to SSH remote host")
    parser.add_argument("root", help="remote path to project root")
    return parser.parse_args(argv)


def _remote(args):
    """ Run this script on a remote machine.

    """
    # The script passes itself to the remote Python interpreter via STDIN, so
    # it must be self-contained. The --host option should be supported here,
    # but forwarding the current value to the remote script yields the local
    # host name, not the remote host name.
    opts = [""]  # force leading delimiter
    if args.config:
        opts.append("config")
    if args.clean:
        opts.append("clean")
    if args.build:
        opts.append("build={:s}".format(args.build))
    command = "python - {:s} {:s}".format(" --".join(opts), args.root)
    if args.ssh:
        command = "ssh {:s} '{:s}".format(args.ssh, command)
    elif args.vagrant:
        # First, make sure VM is running.
        vagrant = "vagrant status {:s}".format(args.vagrant)
        if "running" not in check_output(split(vagrant)):
            vagrant = "vagrant up {:s}".format(args.vagrant)
            check_call(split(vagrant))
        command = "vagrant ssh -c '{:s}' {:s}".format(command, args.vagrant)
    return call(split(command), stdin=open(__file__, "r"))


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
