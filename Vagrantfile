# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # Port 2159 is forwarded for remote debugging. GDB uses the host port, and
  # GDB Server uses the guest port. If there is a port collision, Vagrant will
  # choose different values for these numbers, and the GDB and/or GDB Server
  # configurations must be modified. Run `vagrant port` to see which port
  # numbers have actually been assigned.

  config.ssh.forward_agent = true
  config.vm.box_check_update = true
  config.vm.network :forwarded_port, guest: 2159, host: 2159, auto_correct: true

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "ubuntu/trusty64"
    ubuntu.vm.provision :shell, path: "provision.sh"
  end

end
