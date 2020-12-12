#!/bin/bash

# Convert all images to js files

cd scripts/utilities
echo "Converting images to js files..."
sudo python3 image-to-js.py 
echo "Converted all images to js files."
echo ""

# Purge links

echo "Purging links..."
python3 purge-links.py
echo "Links purged."
echo ""

# Update github repository

echo "Updating github repository: 'KA-CS-Project-Stats'..."
cd ../../

	# Setup: backing up and deleting history

echo "Backing up important files: description..."
sudo cp .git/description description
echo "Removing history and old content..."
sudo rm -rf .git
echo "Reinitializing repository: 'KA-CS-Project-Stats'..."
git init
echo "Copying backup: description into .git..."
sudo cat description > .git/description
sudo rm description
echo "Modifying remote url..."
git remote set-url origin git+ssh://git@github.com/ArrowheadCo/KA-CS-Project-Stats.git
echo "Setup complete."
echo ""

	# Fixing config file

echo "Setting config file..."
git config --global user.email "malksmogendavid2004@gmail.com"
git config --global user.name "ArrowheadCo"
echo "Finished setting up config file."
echo ""

	# Saving changes

echo "Staging changes for repository: 'KA-CS-Project-Stats'..."
git add .
echo "Commiting changes to local git..."
git commit -am "Update: $(date)"
echo "Done saving changes locally."
echo ""

	# Updating github repository

echo "Pushing updates to main repository and wiping github history..."
git push -u --force git+ssh://git@github.com/ArrowheadCo/KA-CS-Project-Stats.git master
echo "Repository: 'KA-CS-Project-Stats' update complete."
echo ""
