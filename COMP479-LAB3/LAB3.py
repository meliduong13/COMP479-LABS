import glob
import os
from pathlib import Path

root_dir = 'C:/Users/melid/shakespeare.mit.edu'

inverted_index = {'Brutus': [], 'Caesar': [], 'Calpurnia': []}

for fullpath in glob.iglob(root_dir + '**/**', recursive=True):
    if os.path.isfile(fullpath):
        filename = Path(fullpath).name
        if 'index.html' not in filename and 'full.html' not in filename and filename.endswith('.html'):
            with open(fullpath, 'r') as file:
                read = file.read()
                for key in inverted_index:
                    if key in read:
                        inverted_index[key].append(filename)

for key in inverted_index:
    print(key + ': ')
    for each in inverted_index[key]:
        print(each, end=", ")
    print('\n')
