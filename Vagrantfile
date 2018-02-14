# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # Port 2159 is forwarded for use with gdbserver. If this port is already in
  # use, Vagrant will choose a different port. Use `vagrant port`

  config.ssh.forward_agent = true
  config.vm.box_check_update = true
  config.vm.network :forwarded_port, guest: 2159, host: 2159, auto_correct: true

  config.vm.define "ubuntu" do |ubuntu|
    ubuntu.vm.box = "ubuntu/trusty64"
    ubuntu.vm.provision :shell, path: "provision.sh"
  end

end
