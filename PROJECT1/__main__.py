from os import listdir
from os.path import isfile, join

from spimi import *

# files = [f for f in glob.glob('.\scrape' + "**/*.html", recursive=True)]
# files = [f for f in listdir('./scrape') if isfile(join('./scrape', f))]


files1 = [f for f in listdir('./scrape1') if isfile(join('./scrape1', f))]
disk_files = [f for f in listdir('./DISK') if isfile(join('./DISK', f))]

import os, fnmatch

files_list = []


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


for filename in find_files('.\scrape', '*.html'):
    files_list.append(filename)


# this is the spimi algorithm which you can call to get your dictionary given a directory of files
# def spimi(reuters_files, block_files, block_files_dir, output_dir_final_dict):
#     tokenize_all(reuters_files=reuters_files, output_dir=block_files_dir)
#     read_files_and_write_final_dict(blocks_produced_from_tokenization=block_files,
#                                     input_dir=block_files_dir, output_dir=output_dir_final_dict)


final_dict_files = [f for f in listdir('./DISK_FINAL') if isfile(join('./DISK_FINAL', f))]

# tokenize_all_crawler(files=files_list, output_dir='./DISK/')
# read_files_and_write_final_dict_crawler(blocks_produced_from_tokenization=disk_files,
#                                         input_dir='./DISK/', output_dir='./DISK_FINAL/')

# run the spimi method in the line below to create your dictionary. Your final dictionary will be distributed over 4
# blocks in the directory 'DISK_FINAL'
# spimi(files, disk_files, './DISK/', './DISK_FINAL/')

# to run spimi in two steps uncomment the lines below. the line above is used to run spimi in 1 shot
# tokenize_all(files, './DISK/')
# read_files_and_write(blocks_produced_from_tokenization=disk_files, input_dir='./DISK/', output_dir='./DISK_FINAL/')

# user input for queries


keep_searching = True
wrong_type = True
query_type = ""
while keep_searching:
    try:
        query_type = input(
            'Choose a query type:\n1. Type "and" for AND query.\n2. Type "or" for OR query.\n3. If you have a single '
            'word query, you can chose either "and" or "or".\n')
        while not (query_type == "and" or query_type == "or"):
            query_type = input('Query type: "and" for AND query, "or" for OR query\n')
        query_search = input('Enter keywords\n')
        search_final_dict(query=query_search, files_dir='./DISK_FINAL/', query_type=query_type)
    except Exception as e:
        print('Error with query')
        print(e)
