#!/bin/bash

all=$(*)

# Clears 'images'

if [ -d "images" ]; then
    echo "Clearing buffer: 'images'..."
    
    # Clear subdirectories

    echo "Clearing subdirectories for 'images'..."
    if [ -d "images/hl" ]; then
        echo "Clearing subdirectory: 'images/hl'..."
        cd images/hl
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'images/hl' does not exist; skipping..."
    fi
    if [ -d "images/tl" ]; then
        echo "Clearing subdirectory: 'images/tl'..."
        cd images/tl
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'images/tl' does not exist; skipping..."
    fi
    if [ -d "images/us" ]; then
        echo "Clearing subdirectory: 'images/us'..."
        cd images/us
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'images/us' does not exist; skipping..."
    fi
    echo ""
else 
    echo "Directory: 'images' does not exist; skipping..."
fi
echo ""

# Clear 'js-info'

if [ -d "js-info" ]; then
    echo "Clearing buffer: 'js-info'..."

    # Clear subdirectories

    echo "Clearing subdirectories for 'js-info'..."
    if [ -d "js-info/hl" ]; then
        echo "Clearing subdirectory: 'js-info/hl'..."
        cd js-info/hl
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'js-info/hl' does not exist; skipping..."
    fi
    if [ -d "js-info/tl" ]; then
        echo "Clearing subdirectory: 'js-info/tl'..."
        cd js-info/tl
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'js-info/tl' does not exist; skipping..."
    fi
    if [ -d "js-info/us" ]; then
        echo "Clearing subdirectory: 'js-info/us'..."
        cd js-info/us
        rm $all
        cd ../../
    else 
        echo "Subdirectory: 'js-info/us' does not exist; skipping..."
    fi
    echo ""
else 
    echo "Directory: 'js-info' does not exist; skipping..."
fi
echo ""

echo "Clearing buffers complete."
echo ""

# Data buffer

echo "If you want to clear the data buffer, you can do so manually."
echo "NOTE: THIS IS NOT RECOMMENDED; YOU WILL LOSE ALL DATA WHEN YOU DO."
echo ""