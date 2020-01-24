# CLion remote docker environment (How to build docker container, run and stop it)
#
# Build and run:
#   docker build -t clion-remote:dev .
#   docker run -d --cap-add SYS_PTRACE -p127.0.0.1:22001:22 --name clion_remote clion-remote:dev
#   ssh-keygen -f "$HOME/.ssh/known_hosts" -R "[localhost]:22001"
#
# stop:
#   docker stop clion_remote_env
# 
# ssh credentials (test user):
#   user@password 

## Adapted from https://github.com/jetbrains/clion-remote


# This build stage creates the container that is used for remote development
# with CLion. It contains the necessary build tools. There is no need to mount
# the local project directory to the container; CLion will (usually...) keep
# the remote files in sync with the local project.

FROM ubuntu:18.04 AS dev

RUN apt-get update \
  && apt-get install -y ssh \
      build-essential \
      gcc \
      g++ \
      gdb \
      clang \
      cmake \
      rsync \
      tar \
      python \
  && apt-get clean

RUN ( \
    echo 'LogLevel DEBUG2'; \
    echo 'PermitRootLogin yes'; \
    echo 'PasswordAuthentication yes'; \
    echo 'Subsystem sftp /usr/lib/openssh/sftp-server'; \
  ) > /etc/ssh/sshd_config_test_clion \
  && mkdir /run/sshd

RUN useradd -m clion \
  && yes password | passwd clion

CMD ["/usr/sbin/sshd", "-D", "-e", "-f", "/etc/ssh/sshd_config_test_clion"]


# This is the final build stage that will create a deployable container.
# Only the built application is carried over from the previous stage, so there
# will not be any build tools installed.

#FROM ubuntu:18.04 as deploy
# TODO: Build Release and copy executable from dev stage to /opt