import requests
import subprocess as subp

#
# Get all filenames
#

hl_files = str(subp.check_output("ls ../../js-info/hl", shell=True))[2:-3].split("\\n")  # Get all hl filenames

for i in hl_files:
	print(requests.get("https://purge.jsdelivr.net/gh/ArrowheadCo/KA-CS-Project-Stats/js-info/hl/{}".format(i))) # Purge needed links

