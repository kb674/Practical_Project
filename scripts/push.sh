#!/bin/bash

echo "push script run"

# login into dockerhub
docker login -u $DOCKERHUB_DETAILS_USR -p password $DOCKERHUB_DETAILS_PSW

# push up kb674/fighter_server_image:latest
docker push kb674/fighter_two_image:latest