=============================
Remote Development With CLion
=============================

.. _remote development: https://youtrack.jetbrains.com/issue/CPP-744
.. _remote debugging: https://www.jetbrains.com/help/clion/remote-debug.html


`Remote development`_ support in CLion is still evolving. As of version 2017.3
there is `remote debugging` support, but no remote project support. This
project is a demonstration of how to use CLion and Vagrant for remote
development.


Project Configuration
=====================

Initial Setup
-------------
1. Clone this project.

.. code-block:: shell

    $ git clone https://github.com/mdklatt/clion-remote.git

2. Open the project in CLion.

3. Define a Python interpreter for the project.

.. |python| image:: doc/image/python.png
   :alt: Python Interpreter configuration

|python|


Remote Builds
-------------

4. Run the build script to configure CMake. The Vagrant box will be started and
   provisioned as necessary.

.. code-block:: shell

    $ python rbuild.py --config --vagrant=ubuntu /vagrant

5. Create a Python run configuration for the build script. This is used to run
   CMake on the Vagrant box to build the project.

.. |rbuild| image:: doc/image/rbuild.png
   :alt: Run Configuration for rbuild.py

|rbuild|


Remote Debugging
----------------

6. Create a Python run configuration for the remote debugging script. This is
   used to run the ``hello`` executable on the Vagrant box using ``gdbserver``.
   The port corresponds to the *guest* port number being forwarded on the
   Vagrant box. Note that the build configuration created above is added as a
   *Before launch* prerequisite.

.. |rdebug| image:: doc/image/rdebug.png
   :alt: Run Configuration for rdebug.py

|rdebug|

7. Create a GDB Remote Debug run configuration for the ``hello`` executable.
   This is used to run the local ``gdb`` cross debugger in concert with
   ``gdbserver``on the Vagrant box. The port number corresponds to the *host*
   number being forwarded to the Vagrant box.

.. |hello| image:: doc/image/hello.png
   :alt: Run Configuration for hello

|hello|
