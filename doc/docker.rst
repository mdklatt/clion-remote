########################################
Remote Development With CLion and Docker
########################################

.. _JetBrains: https://github.com/JetBrains/clion-remote/blob/master/Dockerfile.remote-cpp-env
.. _multi-stage builds: https://docs.docker.com/develop/develop-images/multistage-build
.. _Docker plugin: https://www.jetbrains.com/help/clion/docker.html

.. _video: https://www.youtube.com/watch?v=h69XLiMtCT8

Example of using CLion with Docker container, adapted from `JetBrains`_. This
takes advantage of `multi-stage builds`_ to create dev and deployment images
with a single Dockerfile.

Just as with the Vagrant workflow, it's important to make sure the Docker
container's SSH port does not conflict with other active ports

1. Configure Docker
2. Build container by loading Dockerfile in editor (can't `build --target` this way?)