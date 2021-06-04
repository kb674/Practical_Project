#!/bin/bash

echo "push script run"

# login into dockerhub
docker login -u $DOCKERHUB_DETAILS_USR -p $DOCKERHUB_DETAILS_PSW

# docker-compose push
docker-compose push 
