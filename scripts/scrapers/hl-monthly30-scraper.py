import requests
import datetime as dt
import subprocess as subp
import re

#
# Some settings
#

date = str(dt.datetime.now()).split("-")																# Date today
filename = "hl-monthly30-{}-{}.txt".format(date[0], date[1])															# Filename
filepath = "../../data/hl/{}/{}/{}".format(date[0], date[1], filename)										# Complete file path

array_chars = "[\[ \]\n]"

base_url = "https://khanacademy.org/api/internal/"													# Base url
sort = "3"																								# Refers to the hotlist
limit = "30"																							# Scratchpads to scrape

#
# File structure setup
#

if date[0] not in str(subp.check_output("ls ../../data/hl/", shell=True)):								# If it's a new year
	subp.check_output("mkdir ../../data/hl/{}".format(date[0]), shell=True)								# Make new directory

if date[1] not in str(subp.check_output("ls ../../data/hl/{}".format(date[0]), shell=True)):			# If it's a new month
	subp.check_output("mkdir ../../data/hl/{}/{}".format(date[0], date[1]), shell=True)					# Make new directory

if filename not in str(subp.check_output("ls ../../data/hl/{}/{}".format(date[0], date[1]), shell=True)): # If file isn't there
	subp.check_output("touch ../../data/hl/{}/{}/{}".format(date[0], date[1], filename), shell=True)	# Create new file

if filename.replace(".txt", ".backup.txt") not in str(subp.check_output("ls ../../data/hl/{}/{}".format(date[0], date[1]), shell=True)): # If backup file isn't present
	subp.check_output("touch ../../data/hl/{}/{}/{}".format(date[0], date[1], filename.replace(".txt", ".backup.txt")), shell=True) # Initiate backup file

#
# Read and gather data
#

hl_log = list(i.split(";") for i in open(filepath, 'r').readlines())									# Reads past data
hl_req = requests.get(base_url + "scratchpads/top?sort={}&limit={}".format(sort, limit))				# Makes an API Call to get data
hl_req.raise_for_status()																				# In case of an error
hl_cur = [[i["url"].split('/')[-1], i["title"], 0] for i in hl_req.json()["scratchpads"]] 				# Formats and stores needed data

entry = 0

if len(hl_log):																							# If it isn't the first entry
	entry = int(hl_log[0][0].split("::")[1])															# Gets entry number

#
# Retrieves other details
#

hl_all = [i for i in hl_log if "::" not in i[0]] + [i for i in hl_cur if i[0] not in [j[0] for j in hl_log]] # Combines new and old program id's
index = 0

for i in hl_all:																						# For each id
	p_data = requests.get(base_url + "show_scratchpad?scratchpad_id={}".format(i[0]))					# Get info on program using id
	print(str(p_data))
	if str(p_data) != "<Response [200]>":
		hl_all.remove(i)
	if int(p_data.json()["scratchpad"]["created"].split("-")[1]) == int(date[1]):						# Check if created this month
		i[2] = [int(j) for j in re.sub(array_chars, '', str(i[2])).split(',')]							# Formats array
		if not i[2][-1]:
			i[2] = [0] * entry
		i[2].append(int(p_data.json()["scratchpad"]["sumVotesIncremented"]))	 						# Get number of votes
	else:
		i[2] = [0]
	index += 1

hl_all.sort(key=lambda i: i[2][-1], reverse=True)														# Sorts list

#
# Updates data
#

entry += 1

hl_update = open(filepath, 'w')																			# Opens file
hl_update.write("NEW ENTRY: {}::{}\n".format(str("-".join(date)), str(entry)))							# Appends current time
[hl_update.write("{};{};{}\n".format(i[0], i[1].replace(';', ''), str(i[2]))) for i in hl_all[0:30] if int(i[2][-1])]	# Writes top 30 to file
hl_update.close()																						# Closes file

#
# Creates backup
#

hl_log = open(filepath, 'r')

if len(hl_log.readlines()) < 1: 																		# If something is wrong with file
	hl_log.close()
	subp.check_output("cp {} {}".format(filepath.replace(".txt", ".backup.txt"), filepath), shell=True) # Use backup as file instead
else:
	subp.check_output("cp {} {}".format(filepath, filepath.replace(".txt", ".backup.txt")), shell=True) # Otherwise, do it the other way around
