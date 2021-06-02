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
python3 -m pytest 
