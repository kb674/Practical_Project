#!/bin/bash

echo "deploy script run"

# Send docker-compose file to sawrm manager
scp docker-compose.yaml jenkins@project-swarm-manager:/home/jenkins/

# Send nginx.conf to project-nginx
scp nginx.conf jenkins@project-nginx:/home/jenkins/

# change to jenkins directory run the deploy command
ssh jenkins@project-swarm-manager << EOF 
cd /home/jenkins
docker stack deploy --compose-file docker-compose.yaml service 
EOF

# run nginx container
ssh jenkins@project-nginx << EOF
cd /home/jenkins
docker run -d -p 80:80 --name nginx --mount type=bind,source=$(pwd)/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine
EOF



