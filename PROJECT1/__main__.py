from os import listdir
from os.path import isfile, join

from spimi import *

files = [f for f in listdir('./files') if isfile(join('./files', f))]
files2 = [f for f in listdir('./files2') if isfile(join('./files2', f))]
disk_files = [f for f in listdir('./DISK') if isfile(join('./DISK', f))]


# this is the spimi algorithm which you can call to get your dictionary given a directory of files
def spimi(reuters_files, block_files, block_files_dir, output_dir_final_dict):
    tokenize_all(reuters_files=reuters_files, output_dir=block_files_dir)
    read_all_files_at_once_and_make_final_dict(blocks_produced_from_tokenization=block_files,
                                               input_dir=block_files_dir, output_dir=output_dir_final_dict)


# run the spimi method in the line below to create your dictionary. Your final dictionary will be distributed over 4
# blocks in the directory 'DISK_FINAL'

# spimi(files, disk_files, './DISK/', './DISK_FINAL/')
# tokenize_all(files, './DISK/')
# read_files_and_write(blocks_produced_from_tokenization=disk_files, input_dir='./DISK/', output_dir='./DISK_FINAL/')

# the following test queries are ran on the final dictionary distributed over 4 blocks in the directory 'DISK_FINAL"
final_dict_files = [f for f in listdir('./DISK_FINAL') if isfile(join('./DISK_FINAL', f))]

search_final_dict(query="Jimmy Carter usa", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

# search_final_dict(query="Green Party", files=final_dict_files, files_dir='./DISK_FINAL/',
#                   query_type='and')
#
# search_final_dict(query="Innovation in telecommunications", files=final_dict_files, files_dir='./DISK_FINAL/',
#                   query_type='and')
#
# search_final_dict(query="environmentalist ecologist", files=final_dict_files,
#                   files_dir='./DISK_FINAL/',
#                   query_type='or')
