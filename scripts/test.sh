#!/bin/bash

echo "Test script run"

# create and activate venv
python3 -m venv env
source env/bin/activate

# test server
cd server/
python3 -m pytest 
