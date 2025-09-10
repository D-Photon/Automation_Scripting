# File renaming
import os, sys

source_folder = 'c:/Users/PC/Desktop'

if not os.path.exists(source_folder):
    print('No folder found')
    sys.exit()

print('File exist. Renaming in Progress')

# Loop through location and sort folder to rename
for num, cont in enumerate(os.listdir(source_folder)):
    path = os.path.join(source_folder, cont)
    if not os.path.isdir(path):
        continue

    new_name = os.path.join(source_folder, f'{cont}_{num}')
    if os.path.exists(new_name):
        print('File name already exist...')
        continue
    
    os.rename(path, new_name)
    print(f'Folder {cont} renamed')
    


