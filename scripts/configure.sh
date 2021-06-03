#!/bin/bash

echo "configure script run"

# run ansible playbook
ansible-playbook -i inventory.yaml playbook.yaml
