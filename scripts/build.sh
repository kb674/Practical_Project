#!/bin/bash

echo "build script run"

# build CUSTOM_DB image -  kb674/fighter_db_image:latest
docker build -t kb674/fighter_db_image:latest db

# build SERVER image -  kb674/fighter_server_image:latest
docker build -t kb674/fighter_server_image:latest server

# build SERVICE_TWO image -  kb674/fighter_two_image:latest
docker build -t kb674/fighter_two_image:latest service_two_api

# build SERVICE_THREE image -  kb674/fighter_three_image:latest
docker build -t kb674/fighter_three_image:latest service_three_api

# build SERVICE_FOUR image -  kb674/fighter_four_image:latest
docker build -t kb674/fighter_four_image:latest service_four_api

