#!/bin/bash

echo "deploy script run"

# Send docker-compose file to sawrm manager
scp docker-compose.yaml jenkins@project-swarm-manager:/home/jenkins/

# change to jenkins directory run the deploy command
ssh jenkins@project-swarm-manager << EOF 
cd /home/jenkins
docker stack deploy --compose-file docker-compose.yaml service 
EOF



