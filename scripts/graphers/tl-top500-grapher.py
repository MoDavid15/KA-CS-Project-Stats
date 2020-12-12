import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import subprocess as subp
import re

#
# Some settings
#

date = str(dt.datetime.now()).split("-")                                                                # Date (for hotlist file name)
filename = "tl-top500.txt"                   														    # Filename
filepath = "../../data/tl/{}".format(filename)                  	                                    # Complete file path

array_chars = "[\[ \]\n]"

dpi = 35                                                                                                # Default dpi of picture
size = 12, 7.2                                                                                          # Default size
mode = 'r'                                                                                              # Specifies read mode (so we don't accidentally change anything)

#
# Opens file
#

if filename not in str(subp.check_output("ls ../../data/tl/", shell=True)):								# If file isn't present
	subp.check_output("touch ../../data/tl/{}".format(filename), shell=True)							# Make new file

tl_log = open(filepath, 'r').readlines()                                                                # Opens file
tl_log = [[i.split(';')[0], i.split(';')[1], [int(re.sub(array_chars, '', j)) for j in i.split(';')[2].split(',')]] for i in tl_log if "::" not in i]

#
# Create graphs (if there's data)
#

gen_is_set = False
gen_max = 0
gen_len = 0

if len(tl_log):   

    js_data = open("../../js-info/tl/{}".format(filename.replace(".txt", ".js")), 'w')                  # Creates data file
    js_data.write("const ${} = [\n".format(filename.replace('-', '_')[:-4]))                            # Initiates data file
    [js_data.write("['{}', '{}', {}],\n".format(i[0], i[1].replace('\'', "\\\'"), i[2])) for i in tl_log] # Populates data file
    js_data.write(']')

    
    #
    # For group graphs
    #
    
    all_data = []
    gen_len = 0
    index = 0
    rank = 0

    for i in tl_log:                                                                                    # For each program, graph its data
        if True:

            #
            # Details
            #

            _id = i[0]; name = i[1]; vote_data = i[2] 						        # Gets vote history data

            if index < 30:
                all_data.append(vote_data)																# For cumulative graphs
                if not gen_len:
                    gen_len = len(vote_data)
                index += 1

            maximum = max(vote_data)                                                                    # Data maximum
            minimum = min(vote_data)                                                                    # Data minimum
            y_increment = int(np.ceil((maximum - minimum + 1) / 10))                                    # Y-axis step

            if not gen_is_set:                                                                          # Sets general stuff
                gen_max = max(vote_data) 
                gen_len = len(vote_data)
                gen_is_set = True

            #
            # Individual plots
            #

            fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")       # Creates plot
            plot.plot([i / 8 for i in range(len(vote_data))], vote_data, color="white")                 # Graphs data
            
            plot.set_xlim(0, np.ceil(len(vote_data) / 8))                                               # Sets x-axis range
            plot.set_ylim(min(vote_data), max(vote_data))                                               # Sets y-axis range
            plot.set_xticks([i / 10 * np.ceil(len(vote_data) / 8) for i in range(10)])                  # Sets numbers along x-axis
            plot.set_xlabel("DAYS SINCE NOV 2 2020", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
            plot.set_ylabel("TOTAL NUMBER OF VOTES", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
            plot.set_title(name, {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
            plot.set_facecolor("black")                                                                 # Sets facecolor

            if maximum != minimum:
                plot.set_yticks(range(minimum - y_increment, maximum + 2 * y_increment, y_increment))   # Sets numbers along y-axis
            else:
                plot.set_yticks([minimum])                                                              # In case it didn't change at all
            
            [i.set_color("white") for i in plot.get_xticklabels()]                                      # X-tick colors
            [i.set_color("white") for i in plot.get_yticklabels()]                                      # Y-tick colors
            [i.set_fontsize(18) for i in plot.get_xticklabels()]                                        # X-tick colors
            [i.set_fontsize(18) for i in plot.get_yticklabels()]                                        # Y-tick colors
            [plot.spines[i].set_color("white") for i in plot.spines]                                    # Sets spine color
            plot.ticklabel_format(useOffset=False, style="plain")                                       # Prevents offset and scientific notation use
            
            plt.savefig("../../images/tl/tl-top500-{}.png".format(rank))	                        # Save figure
            plt.close()
            rank += 1

#
# Group plots - stacked
#

fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")     			    # Creates plot
plt.stackplot([i / 72 for i in range(len(vote_data))], all_data)										# Graphs data

plot.set_xlabel("DAYS SINCE MONTH START", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
plot.set_ylabel("CUMULATIVE VOTE COUNT", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
plot.set_title("STACKED AREA - TOPLIST TOP 30", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
plot.set_facecolor("black")																				# Sets facecolor

[i.set_color("white") for i in plot.get_xticklabels()]													# Sets x-ticks colors
[i.set_color("white") for i in plot.get_yticklabels()]													# Sets y-ticks colors
[i.set_fontsize(18) for i in plot.get_xticklabels()]													# Sets x-tick size
[i.set_fontsize(18) for i in plot.get_yticklabels()]													# Sets y-tick size
[plot.spines[i].set_color("white") for i in plot.spines]												# Sets splines color
plot.ticklabel_format(useOffset=False, style="plain")													# Number formatting

plt.savefig("../../images/tl/tl-top30-stack-all.png")

#
# Group plots - bar
#

fig, plot = plt.subplots(figsize=size, dpi=dpi, facecolor="black", edgecolor="black")     			    # Creates plot
plt.bar([str(i) for i in range(1, len(all_data) + 1)], [i[-1] for i in all_data])						# Graphs data

plot.set_xlabel("PROGRAM RANK", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # X-axis label
plot.set_ylabel("LATEST VOTE COUNT", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=24) # Y-axis label
plot.set_title("BAR GRAPH - TOPLIST TOP 30", {"fontname":"Ubuntu Mono"}, fontweight="bold", color="white", fontsize=30) # Sets title
plot.set_facecolor("black")																				# Sets facecolor

[i.set_color("white") for i in plot.get_xticklabels()]													# Sets x-ticks colors
[i.set_color("white") for i in plot.get_yticklabels()]													# Sets y-ticks colors
[i.set_fontsize(18) for i in plot.get_xticklabels()]													# Sets x-tick size
[i.set_fontsize(18) for i in plot.get_yticklabels()]													# Sets y-tick size
[plot.spines[i].set_color("white") for i in plot.spines]												# Sets splines color

plt.savefig("../../images/tl/tl-top30-bar-all.png")
