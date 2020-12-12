#!/bin/bash

# Execute hotlist scraping

cd scripts/scrapers
echo "Scraping: 'hot list monthly 30'..."
sudo python3 hl-monthly30-scraper.py
echo "Scraping: 'top list top 500' complete."
echo ""

# Execute graphing of the data

cd ../graphers
echo "Graphing: 'hot list monthly 30'..."
python3 hl-monthly30-grapher.py
echo "Graphing: 'hot list monthly 30' complete."
echo ""

# Purge links

cd ../utilities
echo "Purging: hot list links..."
#python3 hl-purge-links.py
echo "Purging: hot list links complete."
echo ""

# Return to parent directory

cd ../../
