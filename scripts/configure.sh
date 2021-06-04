#!/bin/bash

echo "configure script run"
# install ansible
sudo apt install ansible

# run ansible playbook
ansible-playbook -i inventory.yaml playbook.yaml
