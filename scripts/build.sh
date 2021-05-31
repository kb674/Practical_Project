#!/bin/bash

echo "build script run"

# build SERVER image -  kb674/fighter_server_image:latest
docker build -t kb674/fighter_server_image:latest server

# push kb674/fighter_server_image:latest
docker push kb674/fighter_two_image:latest
