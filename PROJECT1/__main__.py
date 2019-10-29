from os import listdir
from os.path import isfile, join

from spimi import *

files = [f for f in listdir('./files') if isfile(join('./files', f))]
disk_files = [f for f in listdir('./DISK') if isfile(join('./DISK', f))]


def spimi(reuters_files, block_files, block_files_dir, output_dir_final_dict):
    tokenize_all(reuters_files=reuters_files, output_dir=block_files_dir)
    read_all_files_at_once_and_make_final_dict(blocks_produced_from_tokenization=block_files,
                                               input_dir=block_files_dir, output_dir=output_dir_final_dict)


# run the code in the line below to create your dictionary. Your final dictionary will be distributed over 4 blocks
# in the directory 'DISK_FINAL'
# spimi(files, disk_files, './DISK/', './DISK_FINAL/')


# final test queries are ran on the finl dictionary distributed over 4 blocks in the directory 'DISK_FINAL"
final_dict_files = [f for f in listdir('./DISK_FINAL') if isfile(join('./DISK_FINAL', f))]

search_final_dict(query="Jimmy Carter", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="Green Party", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="Innovations in telecommunication", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="environmentalist ecologist", files=final_dict_files,
                  files_dir='./DISK_FINAL/',
                  query_type='or')
