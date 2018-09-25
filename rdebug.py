""" Run a remote executable.

The executable will be executed with gdbserver, allowing it to be debugged on a
remote machine. This is required for remote debugging using CLion. If this is
running on a Vagrant box, port forwarding must be configured to expose the
guest port gdbserver will be listening on.

  <https://sourceware.org/gdb/onlinedocs/gdb/Server.html>

"""
from argparse import ArgumentParser
from shlex import split
from subprocess import call
from subprocess import check_call
from subprocess import check_output


def main(argv=None):
    """ Script execution.

    """
    args = _args(argv)
    if args.ssh or args.vagrant:
        return _remote(args)
    gdb = split("gdbserver --once :{:s} {:s}".format(args.port, args.target))
    check_call(gdb)  # gdbserver's exit status, not the debugged process
    return 0


def _args(argv=None):
    """ Parse command line arguments.

    By default, sys.argv is parsed.

    """
    # The -h/--help option is defined automatically by argparse.
    parser = ArgumentParser()
    parser.add_argument("-p", "--port", default="2159",
                        help="port gdbserver will listen on")
    remote = parser.add_mutually_exclusive_group()
    remote.add_argument("-V", "--vagrant", help="connect to Vagrant VM box")
    remote.add_argument("-S", "--ssh", help="connect to SSH remote host")
    parser.add_argument("target", help="remote path to executable")
    return parser.parse_args(argv)


def _remote(args):
    """ Run this script on a remote machine.

    """
    # The script passes itself to the remote Python interpreter via STDIN, so
    # it must be self-contained.
    command = "python3 - --port={:s} {:s}".format(args.port, args.target)
    if args.ssh:
        command = "ssh {:s} '{:s}".format(args.ssh, command)
    elif args.vagrant:
        # First, make sure VM is running. Disabled for now because it's slow.
        # vagrant = "vagrant status {:s}".format(args.vagrant)
        # if "running" not in check_output(split(vagrant)):
        #     vagrant = "vagrant up {:s}".format(args.vagrant)
        #     check_call(split(vagrant))
        command = "vagrant ssh -c '{:s}' {:s}".format(command, args.vagrant)
    return call(split(command), stdin=open(__file__, "r"))


# Make the script executable.

if __name__ == "__main__":
    raise SystemExit(main())
