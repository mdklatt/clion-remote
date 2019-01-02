# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
  config.vm.provision :shell, path: "provision.sh"

  clion = true
  if clion
    config.vm.post_up_message = "CLion workarounds enabled"

    # CLion relies on a fixed SSH address, so assign static SSH port here. This
    # must be unique on the host machine.
    port = 22000
    config.vm.post_up_message += "\nUse port #{port} for CLion remote host connection"
    config.vm.network "forwarded_port", id: "ssh", host: port, guest: 22, auto_correct: false

    # CLion only supports SFTP deployments for remote development, so disable
    # folder syncing and let CLion manage the project directory. This means
    # that the contents of the project directory cannot be relied upon while
    # provisioning the VM.
    remote = "/vagrant"
    config.vm.post_up_message += "\nUse #{remote} as the remote deployment directory"
    config.vm.synced_folder ".", remote, disabled: true
    config.vm.provision :shell, inline: "sudo sh -c '(mkdir #{remote} 2>/dev/null && chown vagrant:vagrant #{remote}) || true'"
  end

end
