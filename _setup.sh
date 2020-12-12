#!/bin/bash

# Create file tree

    # images directory

if [ ! -d "images" ]; then
    echo "Creating directory: 'images'..."
    mkdir images
else 
    echo "Directory: 'images' exists; proceeding..."
fi
echo ""

    # images subdirectories

echo "Creating subdirectories for 'images'..."
if [ ! -d "images/hl" ]; then
    echo "Creating subdirectory: 'images/hl'..."
    mkdir images/hl
else 
    echo "Subdirectory: 'images/hl' exists; proceeding..."
fi
if [ ! -d "images/tl" ]; then
    echo "Creating subdirectory: 'images/tl'..."
    mkdir images/tl
else 
    echo "Subdirectory: 'images/tl' exists; proceeding..."
fi
if [ ! -d "images/us" ]; then
    echo "Creating subdirectory: 'images/us'..."
    mkdir images/us
else 
    echo "Subdirectory: 'images/us' exists; proceeding..."
fi
echo ""

    # js-info directory

if [ ! -d "js-info" ]; then
    echo "Creating directory: 'js-info'..."
    mkdir js-info
else 
    echo "Directory: 'js-info' exists; proceeding..."
fi
echo ""

    # js-info subdirectories

echo "Creating subdirectories for 'js-info'..."
if [ ! -d "js-info/hl" ]; then
    echo "Creating subdirectory: 'js-info/hl'..."
    mkdir js-info/hl
else 
    echo "Subdirectory: 'js-info/hl' exists; proceeding..."
fi
if [ ! -d "js-info/tl" ]; then
    echo "Creating subdirectory: 'js-info/tl'..."
    mkdir js-info/tl
else 
    echo "Subdirectory: 'js-info/tl' exists; proceeding..."
fi
if [ ! -d "js-info/tl" ]; then
    echo "Creating subdirectory: 'js-info/us'..."
    mkdir js-info/us
else 
    echo "Subdirectory: 'js-info/us' exists; proceeding..."
fi
echo ""

    # data directory

if [ ! -d "data" ]; then
    echo "Creating directory: 'data'..."
    mkdir data
else 
    echo "Directory: 'data' exists; proceeding..."
fi
echo ""

    # data subdirectories

echo "Creating subdirectories for 'data'..."
if [ ! -d "data/hl" ]; then
    echo "Creating subdirectory: 'data/hl'..."
    mkdir data/hl
else 
    echo "Subdirectory: 'data/hl' exists; proceeding..."
fi
if [ ! -d "data/tl" ]; then
    echo "Creating subdirectory: 'data/tl'..."
    mkdir data/tl
else 
    echo "Subdirectory: 'data/tl' exists; proceeding..."
fi
if [ ! -d "data/tl" ]; then
    echo "Creating subdirectory: 'data/us'..."
    mkdir data/us
else 
    echo "Subdirectory: 'data/us' exists; proceeding..."
fi
echo ""

# Clear buffers

echo "Clearing defined buffers..."
./.clear-buffer.sh
echo "Buffers cleared."
echo ""

# Verify dependencies

    # matplotlib

echo "Verifying module: 'matplotlib'..."
matplotlib=$(pip3 list | grep -w 'matplotlib')
echo $matplotlib

if [ ${#matplotlib} -lt 1 ]; then 
    echo "Module: 'matplotlib' not found; installing module..."
    pip3 install matplotlib
else 
    echo "Module: 'matplotlib' verfied; proceeding..."
fi
echo ""

    # numpy

echo "Verifying module: 'numpy'..."
numpy=$(pip3 list | grep -w 'numpy')
echo $numpy

if [ ${#numpy} -lt 1 ]; then 
    echo "Module: 'numpy' not found; installing module..."
    pip3 install numpy
else 
    echo "Module: 'numpy' verfied; proceeding..."
fi
echo ""

    # requests

echo "Verifying module: 'requests'..."
requests=$(pip3 list | grep -w 'requests')
echo $requests

if [ ${#requests} -lt 1 ]; then 
    echo "Module: 'requests' not found; installing module..."
    pip3 install requests
else 
    echo "Module: 'requests' verfied; proceeding..."
fi
echo ""

    # Pillow

echo "Verifying module: 'Pillow'..."
Pillow=$(pip3 list | grep -w 'Pillow')
echo $Pillow

if [ ${#Pillow} -lt 1 ]; then 
    echo "Module: 'Pillow' not found; installing module..."
    pip3 install Pillow
else 
    echo "Module: 'Pillow' verfied; proceeding..."
fi
echo ""

    # Git

echo "Verifying application: 'git'..."
Git=$(git --version | grep -w 'git')
echo $Git

if [ ${#Git} -lt 1 ]; then 
    echo "Module: 'git' not found; installing module..."
    apt install git
else 
    echo "Module: 'git' verfied; proceeding..."
fi
echo ""

# Make other files executable

echo "Making shell files executable..."
chmod +xwr .clear-buffer.sh
chmod +xwr .cron-config.sh
chmod +xwr hl.sh
chmod +xwr tl.sh 
chmod +xwr gh.sh
echo ""

echo "###                   ###"
echo "### USER INSTRUCTIONS ###"
echo "###                   ###"
echo ""

# Setup permissions

echo "Setting up permissions..."
echo "Please type:"
echo "	sudo visudo"
echo "then input the following line:"
echo "	username ALL=(ALL) NOPASSWD: $(pwd)/gh.sh"
echo "to enable ./gh.sh to execute properly."
echo ""

# Setup and configure cron

echo "Reconfiguring cron file..."
echo "Please type:" 
echo "	sudo cat ./.cron-config.sh >> /etc/crontab"
echo "to configure cron file."
echo ""

# Setup done
echo "Setup finished."
echo ""

echo "NOTE: FOLLOW THE INSTRUCTIONS ABOVE IF YOU HAVEN'T"
echo ""
