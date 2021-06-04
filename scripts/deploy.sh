#!/bin/bash

echo "deploy script run"

# Send docker-compose file to sawrm manager
scp docker-compose.yaml jenkins@project-swarm-manager:/home/jenkins/

# change to jenkins directory run the deploy command
ssh jenkins@project-swarm-manager << EOF 
cd /home/jenkins
export DATABASE_URI=${DATABASE_URI}
docker stack deploy --compose-file docker-compose.yaml service 
EOF

# Send nginx.conf to project-nginx
scp nginx.conf jenkins@project-nginx:/home/jenkins/

# run nginx container
#docker run -d -p 80:80 --name nginx --mount type=bind,source=/home/jenkins/nginx.conf,target=/etc/nginx/nginx.conf nginx:alpine
# start the container
ssh jenkins@project-nginx << EOF
cd /home/jenkins
docker start nginx
EOF

