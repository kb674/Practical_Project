#!/bin/bash

echo "build script run"

#build server image called: kb674/fighter_server_image:latest
docker build -t kb674/fighter_server_image:latest /server
