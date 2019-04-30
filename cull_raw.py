# Thomas Nabelek, April 2019
# github.com/nabelekt

# A script to remove raw image files which have no corresponding compressed image file in the same directory

import sys
from os import listdir, remove
from os.path import isfile, join

comp_ext = 'JPG'
raw_ext = 'NEF'

if len(sys.argv) < 2:
    exit(f"\nERROR: Photo directory not specified. Usage: {sys.argv[0]} [path to directory with ending slash]\nExiting.\n\n")

photo_dir = sys.argv[1]

# Get list of files in directory
file_and_dir_list = listdir(photo_dir)

# Exclude subdirectories from list
file_list = [f for f in file_and_dir_list if isfile(join(photo_dir, f))]

# Narrow file list to RAW images
raw_images = [s for s in file_list if raw_ext in s]

# Narrow file list to compressed images
comp_images = [s for s in file_list if comp_ext in s]

for file in raw_images:
    filename = file[0:file.find(raw_ext)-1]
    comp_file = filename + '.' + comp_ext
    raw_file = filename + '.' + raw_ext
    if comp_file in comp_images:
        print(comp_file + ' found. Keeping ' + filename + '.' + raw_ext + ".")
    else:
        print(comp_file + ' found. Removing ' + filename + '.' + raw_ext + '... ', end="")
        try:
            remove(photo_dir + raw_file)
            print("done.")
        except Exception as e:
            print("FAILURE!")
            print(e)

