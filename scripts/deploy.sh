#!/bin/bash

echo "deploy script run"

# send docker-compose file to swarm-manager
scp docker-compose.yaml project-swarm-manager


