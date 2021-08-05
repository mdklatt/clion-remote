# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "provision.sh"

  # CLion relies on a fixed SSH address, so assign static SSH port here. This
  # must be unique on the host machine.
  port = 22000
  config.vm.post_up_message = "\nUse port #{port} for CLion remote host connection"
  config.vm.network "forwarded_port", id: "ssh", host: port, guest: 22, auto_correct: false

end
