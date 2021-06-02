#!/bin/bash

echo "Test script run"

# create and activate venv
python3 -m venv env
source env/bin/activate

# install dependencies
pip3 install pytest
pip3 install requests-mock
pip3 install flask
pip3 install flask-sqlalchemy
pip3 install flask-testing

# test server
cd server/
python3 -m pytest --doctest-modules --junitxml=junit/test-results.xml --cov=application --cov-report=xml --cov-report=html
cd ..

# test ervice_two_api
cd service_two_api
python3 -m pytest 
cd ..

# test service_three_api
cd service_three_api
python3 -m pytest 
cd ..

# test service_four_api
cd service_four_api
python3 -m pytest 
cd ..



