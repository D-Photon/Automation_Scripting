# File moving script

import os, shutil, sys
from pathlib import Path

# FOlders
source_folder = 'c:/Users/PC/Desktop'
dest_path = 'C:/Users/PC/Desktop/New folder (2)/PROJECTS/Rashid/Finance'

file_ext = {'Text':'.txt', 'Doc':'.docx'}

# Check folder
if not os.path.exists(source_folder):
    print('Directory not exist.')
    sys.exit()

# Make new directory (sub_folders in the destination dir)
for key in file_ext.keys():
    new_path = os.path.join(dest_path, key)
    os.makedirs(new_path, exist_ok=True)

# List out the source folder contents
moved = False
for cont in os.listdir(source_folder):
    if os.path.isdir(os.path.join(source_folder, cont)):
        continue
    # Extract ext and compare
    ext = os.path.splitext(cont)[1]

    for key, value in file_ext.items():
        if ext.lower() == value:
            
            file_dest_path = os.path.join(dest_path, key)
            file_path = os.path.join(source_folder, cont)
            shutil.move(file_path, file_dest_path)
            print(f'File {cont} successfully moved to {key} folder')
            moved = True

if not moved:
    print('No file moved')
    