import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import subprocess as subp
import re

#
# Some settings
#

date = str(dt.datetime.now()).split("-")                                                                # Date (for hotlist file name)
filename = "hl-monthly30-{}-{}.txt".format(date[0], date[1])											# Filename
filepath = "../../data/hl/{}/{}/{}".format(date[0], date[1], filename)	                                # Complete file path

array_chars = "[\[ \]\n]"

dpi = 35                                                                                         		# Default dpi of picture
size = 12, 7.2																							# Default size	
mode = 'r'                                                                                              # Specifies read mode (so we don't accidentally change anything)

#
# Opens file
#

if date[0] not in str(subp.check_output("ls ../../data/hl/", shell=True)):								# If it's a new year
	subp.check_output("mkdir ../../data/hl/{}".format(date[0]), shell=True)								# Make new directory

if date[1] not in str(subp.check_output("ls ../../data/hl/{}".format(date[0]), shell=True)):			# If it's a new month
	subp.check_output("mkdir ../../data/hl/{}/{}".format(date[0], date[1]), shell=True)					# Make new directory

if filename not in str(subp.check_output("ls ../../data/hl/{}/{}".format(date[0], date[1]), shell=True)): # If file isn't there
	subp.check_output("touch ../../data/hl/{}/{}/{}".format(date[0], date[1], filename), shell=True)	# Create new file

hl_log = [i.split(';') for i in open(filepath, 'r').readlines() if "::" not in i]						# Opens file
hl_log = [[i[0], i[1], re.sub(array_chars, '', i[2]).split(',')] for i in hl_log]						# Formats data

#
# Create graphs and data file (if there's data)
#

if len(hl_log):																							# If there's data

	js_data = open("../../js-info/hl/{}".format(filename.replace(".txt", ".js")), 'w')                  # Creates data file
	js_data.write("const ${} = [\n".format(filename.replace('-', '_')[:-4]))                            # Initiates data file
	[js_data.write("['{}', '{}', {}],\n".format(i[0], i[1].replace('\'', "\\\'"), i[2])) for i in hl_log] # Populates data file
	js_data.write(']')

	all_data = []
	gen_len = 0
	index = 0

	for i in hl_log:
		#
		# Details
		#

		_id = i[0]                                                                       				# Gets program id
		name = i[1]																						# Gets program name
		vote_data = [int(j) for j in i[2]]																# Gets vote data 
		offset = max(0.01 * max(vote_data), 1)															# Gets offset from edges

		all_data.append(vote_data)																		# For cumulative graphs
		if not gen_len:
			gen_len = len(vote_data)																	# Basis for cumulative graphs

		#
		# Individual Graphs
		#

		fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")     		# Creates plot
		plot.plot([i / 72 for i in range(len(vote_data))], vote_data, color="white")						# Graphs data

		plot.set_xlim(0, np.ceil(len(vote_data) / 72))													# Sets x-axis range
		plot.set_ylim(min(vote_data) - offset, max(vote_data) + offset)									# Sets y-axis range
		plot.set_xticks([i / 10 * np.ceil(len(vote_data) / 72) for i in range(10)])						# Sets numbers along x-axis
		plot.set_xlabel("DAYS SINCE MONTH START", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
		plot.set_ylabel("TOTAL NUMBER OF VOTES", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
		plot.set_title(name, {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
		plot.set_facecolor("black")																		# Sets facecolor
		
		[i.set_color("white") for i in plot.get_xticklabels()]											# Sets x-ticks colors
		[i.set_color("white") for i in plot.get_yticklabels()]											# Sets y-ticks colors
		[i.set_fontsize(18) for i in plot.get_xticklabels()]											# Sets x-tick size
		[i.set_fontsize(18) for i in plot.get_yticklabels()]											# Sets y-tick size
		[plot.spines[i].set_color("white") for i in plot.spines]										# Sets splines color
		plot.ticklabel_format(useOffset=False, style="plain")											# Number formatting

		print('saving file')
		plt.savefig("../../images/hl/hl-monthly30-{}-{}.png".format(date[0], date[1]))
		print("../../images/hl/hl-monthly30-{}-{}.png".format(date[0], date[1]))
		plt.close()
		index += 1

#
# Group plots - bar
#

fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")     				# Creates plot
plt.bar([str(i) for i in range(1, len(all_data) + 1)], [i[-1] for i in all_data])						# Graphs data

plot.set_xlabel("PROGRAM RANK", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
plot.set_ylabel("LATEST VOTE COUNT", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
plot.set_title("BAR GRAPH - HOTLIST MONTHLY 30", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
plot.set_facecolor("black")																				# Sets facecolor

[i.set_color("white") for i in plot.get_xticklabels()]													# Sets x-ticks colors
[i.set_color("white") for i in plot.get_yticklabels()]													# Sets y-ticks colors
[i.set_fontsize(18) for i in plot.get_xticklabels()]													# Sets x-tick size
[i.set_fontsize(18) for i in plot.get_yticklabels()]													# Sets y-tick size
[plot.spines[i].set_color("white") for i in plot.spines]												# Sets splines color

plt.savefig("../../images/hl/{}".format(filename.replace(".txt", "-bar-all.png")))

#
# Group plots - stacked
#

fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")     				# Creates plot
print(all_data)
plt.stackplot([int(i) / 72 for i in range(len(vote_data))], all_data)										# Graphs data

plot.set_xlabel("DAYS SINCE MONTH START", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
plot.set_ylabel("CUMULATIVE VOTE COUNT", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
plot.set_title("STACKED AREA - HOTLIST MONTHLY 30", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
plot.set_facecolor("black")																				# Sets facecolor

[i.set_color("white") for i in plot.get_xticklabels()]													# Sets x-ticks colors
[i.set_color("white") for i in plot.get_yticklabels()]													# Sets y-ticks colors
[i.set_fontsize(18) for i in plot.get_xticklabels()]													# Sets x-tick size
[i.set_fontsize(18) for i in plot.get_yticklabels()]													# Sets y-tick size
[plot.spines[i].set_color("white") for i in plot.spines]												# Sets splines color
plot.ticklabel_format(useOffset=False, style="plain")													# Number formatting

plt.savefig("../../images/hl/{}".format(filename.replace(".txt", "-stack-all.png")))
