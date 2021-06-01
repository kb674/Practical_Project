#!/bin/bash

echo "deploy script run"

# run ansible playbook
ansible-playbook -i inventory.yaml playbook.yaml
