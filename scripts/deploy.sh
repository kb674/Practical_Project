#!/bin/bash

echo "deploy script run"

# send docker-compose file to swarm-manager
scp docker-compose.yaml project-swarm-manager

# ssh heredoc command
ssh kusha@project-swarm-manager << EOF
docker stack deploy --compose-file docker-compose.yaml service
EOF


