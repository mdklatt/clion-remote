#########################################
Remote Development With CLion and Vagrant
#########################################

.. _remote development: https://blog.jetbrains.com/clion/2018/11/clion-2018-3-remote-dev-cpu-profilers-cpp17/#remote_development
.. _Vagrant: https://www.vagrantup.com
.. _2018.2: https://github.com/mdklatt/clion-remote/tree/2018.2
.. _Vagrant support: https://youtrack.jetbrains.com/issue/CPP-7671


This project is an example of using the new `remote development`_ features of
CLion 2018.3 with a `Vagrant`_ VM as the remote host. See the `2018.2`_ branch
for using earlier versions of CLion that support remote debugging but not
remote builds.

CLion does not have `Vagrant support`_ yet, so some modifications to the
standard Vagrant workflow are necessary; see the project ``Vagrantfile``. The
Vagrant box must be Linux, and it must have rsync and a recent version of
GDB (7.8+). Newer versions of Ubuntu include a compatible version of GDB in
their standard package repos, but CentOS users will have to build a version
from source.


=============
Initial Setup
=============

1. Clone this project.

2. Start and provision the Vagrant box. Note the connection port and remote
project directory in the Vagrant start-up messages.

.. code-block:: shell

    $ vagrant up

    ...

    ==> default: CLion workarounds enabled
    ==> default: Use port 22000 for CLion remote host connection
    ==> default: Use /vagrant as the remote deployment directory


=====================
Project Configuration
=====================

.. _static IP: https://www.vagrantup.com/docs/networking/private_network.html#static-ip
.. _mounted folders: https://youtrack.jetbrains.com/issue/CPP-14887

.. |Toolchains| image:: doc/image/Toolchains.png
   :alt: Toolchains

.. |Credentials| image:: doc/image/Credentials.png
   :alt: Remote Host Credentials

.. |CMake| image:: doc/image/CMake.png
   :alt: CMake Profiles

.. |Deployment| image:: doc/image/Deployment.png
   :alt: Remote Deployment

.. |Mappings| image:: doc/image/Mappings.png
   :alt: Mappings

.. |Excluded| image:: doc/image/Excluded.png
   :alt: Excluded Paths


3. Define a Toolchain to configure the build and debug tools for the Vagrant
   box. Here, a fixed SSH port is used to connect. A `static IP`_ can be
   instead. In either case, the address must be unique on the local machine.

   |Toolchains|

   Use the Vagrant private key file for this connection.

   |Credentials|

   Once the Toolchain is configured, hit ``Apply`` to create it.


4. Define one or more CMake Profiles to configure the build types to use with
   the Vagrant Toolchain.

   |CMake|


5. When a remote Toolchain is created, CLion will create the corresponding SFTP
   deployment. CLion does not yet support `mounted folders`_ for remote builds,
   so a Vagrant synced folder cannot be used for the project directory.

   |Deployment|

   The local project is directory is mapped to ``/vagrant`` on the VM. Here,
   CLion will manage the remote directory, not Vagrant. This means that
   ``/vagrant`` will be empty during provisioning.

   |Mappings|

   CLion will automatically exclude the local build directory from syncing, but
   all other exclusions must be manually configured. The local ``.vagrant/``
   directory should be excluded along with any other files that are not needed
   to build or run the project.

   |Excluded|


===============
Remote Workflow
===============

.. |hello| image:: doc/image/hello.png
   :alt: hello Run/Debug Configuration

.. |debug| image:: doc/image/debug.png
   :alt: hello Run/Debug Configuration

Once the project is properly configured, CLion will sync files to the Vagrant
VM and run CMake to build the project model. Run/Debug Configurations will be
created for all of the project executables.

|hello|

CLion can now be used to edit, build, debug, and test the project as if it was
on the local machine.

|debug|

Project binaries built on the remote machine will be available in the local
copy of the build directory.


===============
Troubleshooting
===============

.. _YouTrack: https://youtrack.jetbrains.com/issues/CPP
.. _CPP-744: https://youtrack.jetbrains.com/issue/CPP-744

Use `YouTrack`_ to report new bugs, find workarounds for existing bugs, and
make feature requests. Many remote development bugs are attached to `CPP-744`_.

For best results with a Vagrant remote host, the VM should be running before
opening the project in CLion. Still, it's possible for the project to get in
an inconsistent state that will affect file syncing.

Suggested solutions include:

- Run ``Tools->CMake->Reload CMake Project``
- Run ``Tools->CMake->Reset Cache and Reload Project``
- Run ``File->Invalidate Caches / Restart``
- Restart the Vagrant VM
- Delete the Toolchain configuration and recreate it
