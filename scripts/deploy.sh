#!/bin/bash

echo "deploy script run"

# run ansible playbook
sudo su jenkins
ansible-playbook -i inventory.yaml playbook.yaml
