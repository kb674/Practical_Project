#! bin/bash

# build server
docker build -t server_image server
# build api for each service
docker build -t service_two_api_image service_two_api
docker build -t service_three_api_image service_three_api
docker build -t service_four_api_image service_four_api
# create network
docker network create fight_network
# run containers
docker run -d -p 5000:5000 --network fight_network --name server server_image
docker run -d --network fight_network --name service_two_api service_two_api_image
docker run -d --network fight_network --name service_three_api service_three_api_image
docker run -d --network fight_network --name service_four_api service_four_api_image