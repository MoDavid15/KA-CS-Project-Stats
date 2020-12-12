import requests
import datetime as dt
import subprocess as subp
import re

#
# Some settings
#

date = str(dt.datetime.now()).split("-")																# Date today
filename = "tl-top500.txt"																				# Filename
filepath = "../../data/tl/{}".format(filename)																# Complete file path

array_chars = "[\[ \]\n]"

base_url = "https://www.khanacademy.org/api/internal/"													# Base url
sort = "5"																								# Refers to the hotlist
limit = "500"                                                                                           # Scratchpads to scrape   
topic_id = "xffde7c31"																					# Topic id (?)

#
# File structure setup
#

if filename not in str(subp.check_output("ls ../../data/tl/", shell=True)):								# If file isn't present
	subp.check_output("touch ../../data/tl/{}".format(filename), shell=True)							# Make new file

if filename.replace(".txt", ".backup.txt") not in str(subp.check_output("ls ../../data/tl/", shell=True)): # If backup file isn't present
	subp.check_output("touch ../../data/tl/{}".format(filename.replace(".txt", ".backup.txt")), shell=True) # Initiate backup file

#
# Read and gather data
#

file = open(filepath, 'r').readlines()
entry = 0

if len(file):																							# If it isn't the first entry
	entry = int(file[0].split("::")[1])																	# Gets entry number

tl_log = { i.split(';')[0] : {																			# New item (based on program id)
	"name" : i.split(';')[1],																			# Property: program title
	"vote" : i.split(';')[2].split(','),																# Property: vote history
	"date" : i.split(';')[3],																			# Property: date created 
	"user" : i.split(';')[4]																			# Property: user id
} for i in open(filepath, 'r').readlines() if "::" not in i}									# Reads past data and stores in dictionary

tl_req = requests.get(base_url + "scratchpads/top?sort={}&limit={}&topic_id={}".format(sort, limit, topic_id)) # Makes an API Call to get data
tl_req.raise_for_status()																				# In case of an error

tl_cur = { i["url"].split('/')[-1] : {
	"name" : i["title"].replace(';', ''),
	"vote" : [int(i["sumVotesIncremented"])],
	"date" : i["created"],
	"user" : i["authorKaid"]
} for i in tl_req.json()["scratchpads"]}																# Gathers and formats data from request

#
# Retrieves other details
#

tl_all = {}

for i in tl_cur:
	old = ["0"] * entry if i not in tl_log else tl_log[i]["vote"]										# Gets old number of votes
	old = [int(re.sub(array_chars, '', i)) for i in old]												# Vote array or something
	tl_all[i] = {
		"name" : tl_cur[i]["name"],
		"vote" : old + tl_cur[i]["vote"],
		"date" : tl_cur[i]["date"],
		"user" : tl_cur[i]["user"]
	}																									# Updates list

#
# Updates data
#

entry += 1																								# Next entry
tl_update = open(filepath, 'w')																			# Opens file
tl_update.write("NEW ENTRY: {}::{}\n".format(str("-".join(date)), str(entry)))							# Specifies new entry
[tl_update.write("{};{};{};{};{}\n".format(i, tl_all[i]["name"], tl_all[i]["vote"], tl_all[i]["date"], tl_all[i]["user"])) for i in tl_all] # Writes to file
tl_update.close()																						# Closes file

#
# Creates backup
#

tl_log = open(filepath, 'r')

if len(tl_log.readlines()) != int(limit) + 1:															# If something is wrong with file
	tl_log.close()
	subp.check_output("cp {} {}".format(filepath.replace(".txt", ".backup.txt"), filepath), shell=True) # Use backup as file instead
else:
	subp.check_output("cp {} {}".format(filepath, filepath.replace(".txt", ".backup.txt")), shell=True) # Otherwise, do it the other way around
