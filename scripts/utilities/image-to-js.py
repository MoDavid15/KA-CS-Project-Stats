from PIL import Image
import subprocess as subp

#
# Some settings
#

hl_files = str(subp.check_output("ls ../../images/hl", shell=True))[2:-3].split("\\n")  # Get all hl filenames
tl_files = str(subp.check_output("ls ../../images/tl", shell=True))[2:-3].split("\\n")  # Get all tl filenames
mode = 'r'                                                                              # We don't want to overwrite files                                                                              # Counts strings of zeros

size = 12, 7.2
dpi = 35

#
# Hot list files
#

for i in hl_files:
    img = Image.open("../../images/hl/{}".format(i), mode)                              # Opens file
    pixels = list(img.getdata())                                                        # Pixel data
    compressed = []                                                                     # Converts to gray scale
    strand = 0
    
    for j in pixels:                                                                    # Compresses data
        newval = (j[0] + j[1] + j[2]) / 3                                               # Gray scale value
        if newval != 0:
            if strand:
                compressed = compressed[:-strand] + [str(strand), newval]               # Run-length encoding
                strand = 0
            else:
                compressed.append(newval)
        else:
            strand += 1
            compressed.append(float(newval))                                            # Just add it lol
    if strand:                                                                          # In case last element was a 0
        compressed = compressed[:-strand] + [str(strand)]

    js_img = open("../../js-info/hl/{}".format(i.replace(".png", ".js")), 'w')          # Js file for data
    js_img.write("const ${} = {}".format(i.replace('-', '_')[:-4], '{'))                # Write data to file
    js_img.write("img_data : {},".format(str(compressed).replace(' ', '')))             # Add img_data key
    js_img.write("width : {}, height : {}, id : '{}'".format(str(size[0] * dpi), str(size[1] * dpi), i.split('-')[-1].split('.')[0])) # Specifies other details
    js_img.write("}")

#
# Top list files
#

for i in tl_files:
    img = Image.open("../../images/tl/{}".format(i), mode)                              # Opens file
    pixels = list(img.getdata())                                                        # Pixel data
    compressed = []                                                                     # Converts to gray scale
    strand = 0

    for j in pixels:                                                                    # Compresses data
        newval = (j[0] + j[1] + j[2]) / 3                                               # Gray scale value
        if newval != 0:
            if strand:
                compressed = compressed[:-strand] + [str(strand), newval]               # Run-length encoding
                strand = 0
            else:
                compressed.append(newval)
        else:
            strand += 1
            compressed.append(float(newval))                                            # Just add it lol
    if strand:                                                                          # In case last element was a 0
        compressed = compressed[:-strand] + [str(strand)]

    js_img = open("../../js-info/tl/{}".format(i.replace(".png", ".js")), 'w')          # Js file for data
    js_img.write("const ${} = {}".format(i.replace('-', '_')[:-4], '{'))                # Write data to file
    js_img.write("img_data : {},".format(str(compressed).replace(' ', '')))                   # Add img_data key
    js_img.write("width : {}, height : {}, id : '{}'".format(str(size[0] * dpi), str(size[1] * dpi), i.split('-')[-1].split('.')[0])) # Specifies other details
    js_img.write("}")
