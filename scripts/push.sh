#!/bin/bash

echo "push script run"

# login into dockerhub
docker login -u $DOCKER_USER_NAME -p password $DOCKER_PASSWORD

# push up kb674/fighter_server_image:latest
docker push kb674/fighter_two_image:latest
