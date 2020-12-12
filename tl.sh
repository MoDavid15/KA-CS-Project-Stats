#!/bin/bash

# Execute toplist scraping

cd scripts/scrapers
echo "Scraping: 'top list top 500'..."
sudo python3 tl-top500-scraper.py
echo "Scraping: 'top list top 500' complete."
echo ""

# Execute graphing of the data

cd ../graphers
echo "Graphing: 'top list top 500'..."
python3 tl-top500-grapher.py
echo "Graphing: 'top list top 500' complete."
echo ""

# Purge links

cd ../utilities
echo "Purging: top list links..."
#python3 tl-purge-links.py
echo "Purging: top list links complete."
echo ""

# Return to parent directory

cd ../../
