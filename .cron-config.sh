#!/bin/bash

path=$(pwd)
user=$(whoami)

# Clear daily logs and title

echo ""
echo "#########################################################################"
echo "# KA-CS-Project-Stats Cron Jobs #########################################"
echo "#########################################################################"
echo ""

echo " 0  0 * * * $user cd $path && echo 'DAY START \$(date)' > .logs.txt"
echo ""

# Hot list scraper

echo " 0  * * * * $user cd $path && ./hl.sh >> .logs.txt"
echo "20  * * * * $user cd $path && ./hl.sh >> .logs.txt"
echo "40  * * * * $user cd $path && ./hl.sh >> .logs.txt"
echo ""

# Top list scraper

echo " 0  0 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0  3 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0  6 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0  9 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0 12 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0 15 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0 18 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo " 0 21 * * * $user cd $path && ./tl.sh >> .logs.txt"
echo ""

# Github update

echo " 0  * * * * $user cd $path && ./gh.sh >> .logs.txt"
echo "30  * * * * $user cd $path && ./gh.sh >> .logs.txt"
echo ""
echo "#########################################################################"
echo "#########################################################################"
echo ""
