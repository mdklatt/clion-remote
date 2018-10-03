# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # CLion does not yet support Vagrant directly, so assign a static IP address
  # to use as the host address for a remote toolchain configuration. Every
  # Vagrant box should have it's own unique address to minimize the chance of
  # IP conflicts on the local network.
  #
  # It's possible to use localhost:NNNN instead of an IP address, but it's
  # important to make sure each Vagrant box is using a unique static port for
  # SSH in this case, i.e. don't use `auto_correct` for SSH ports.

  config.vm.network "private_network", ip: "192.168.237.50"

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "ubuntu/bionic64"  # 18.04
    ubuntu.vm.provision :shell, path: "provision.sh"
  end

end
