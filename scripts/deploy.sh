#!/bin/bash

echo "deploy script run"

# run ansible playbook
ansible-playbbok -i inventory.yaml playbook.yaml
