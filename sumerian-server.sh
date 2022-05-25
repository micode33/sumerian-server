#!/bin/bash

# Setup python environment in the Code directory
python3 -m venv Code

# Change directory to Code
cd Code

# Activate the python environment
source bin/activate

# Install git
sudo yum -y install git

# Clone the repo
git clone https://github.com/micode33/sumerian-server.git

# Change directory to sumerian-server
cd sumerian-server

# Disable httpd which is listening on port 80
sudo systemctl stop httpd

# Allow httpd to shutdown
sleep 5

# Run sumerian server on port 90
sudo python3 main.py -p 80