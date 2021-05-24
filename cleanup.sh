#! bin/bash
docker rm -f server service_two_api service_three_api

docker rmi server_image service_two_api_image service_three_api_image

docker network rm fight_network


