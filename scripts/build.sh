#!/bin/bash

echo "build script run"

# build SERVER image -  kb674/fighter_server_image:latest
docker build -t kb674/fighter_server_image:latest server


