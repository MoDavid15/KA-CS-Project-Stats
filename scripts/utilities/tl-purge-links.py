import requests
import subprocess as subp

#
# Get all filenames
#

tl_files = str(subp.check_output("ls ../../js-info/tl", shell=True))[2:-3].split("\\n")  # Get all tl filenames

for i in tl_files:
	print(requests.get("https://purge.jsdelivr.net/gh/ArrowheadCo/KA-CS-Project-Stats/js-info/tl/{}".format(i))) # Purge needed links
