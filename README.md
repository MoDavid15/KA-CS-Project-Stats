# KA CS Project Stats

**KA CS Project Stats** scrapes Khan Academy's internal scratchpads every now and then to gather data on user projects and the like. Summary statistics and graphs are then generated via python scripts, and subsequently uploaded to this repository. The updates occur every approximately thirty minutes.

# Project Status

Version 0.1 is the current version of this project.

Currently, most of the scripts used in the execution of the project are a little messy and unoptimized; although the shell scripts are a little cleaner, the python scripts in particular need to be reformatted and modified.

Hot list scraping is present; top list scraping is also on-going; however, user statistics have not been implemented.

# Project Webpage

Visit the [KA CS Project Stats](https://www.khanacademy.org/computer-programming/i/6548984783650816?width=480&height=640) webpage on **Khan Academy** (KA) for a more detailed explanation on the nature of the project and its mechanism. The accumulated data are also displayed on the said page.

# Project Files & Directories

### Directory: data

This directory contains all the scraped data. 

Under the **hl subdirectory**, the file structure consists of year and month subfolders. These then store the monthly data associated with the hot list (along with their backup files).

Under the **tl subdirectory**, a single file with data on the top 500 programs stores the top list data. A backup file also accompanies this file.

### Directory: images

This directory contains the graphs for the various data obtained by the scraping scripts. The images are generated via Python's matplotlib module and its graphing capabilities.

### Directory: js-info

The file structure of this directory follows that of the **images directory**. This folder mainly contains the pixel data of the the png files in the aforementioned folder but transcribed unto a javascript file for the sake of importing them into KA webpages. Run-length encoding for contingent zero values is utilized to minimize the size of the file.

### Directory: scripts

The scripts which execute the primary tasks of the project are located here. Hence, aptly-named subfolders will be found, such as the **scrapers subdirectory** and the **graphers subdirectory**. These speak for themselves.

On the other hand, there is also the **utilities subdirectory** also located within. These contain some general tasks coded in python, such as purging jsdelivr resource links and .png -> .js conversion.

### File: _setup.sh

This file initiates the project directory when cloning the project on a new device (currently, only Linux devices are supported).

It sets up (and clears) the file structure (**data directory** not included) and verifies the existence of the necessary dependencies. It then tells the user to update the cron file and grant it sudo privileges.

### File: .logs.txt

The output of each action is appended on to this text file. However, cron is asked to clear this file at the end of each day (00:00 UTC).

# Why is there no commit history?

Github repositories follow a size limit (usually 1-2GB). Every time changes are pushed, the past versions of the files are not discarded; this is a helpful feature, especially for developers who may need to revisit versions or track changes. However, that contributes significantly to the size of the repository. Thus, I have decided to disable it.

# Contributions

To contribute, message the author of this project. Additionally, report any issues as soon as possible.

# Discord Server

_Coming soon!_
