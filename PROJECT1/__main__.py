from os import listdir
from os.path import isfile, join

from spimi import *

files = [f for f in listdir('./files') if isfile(join('./files', f))]
disk_files = [f for f in listdir('./DISK') if isfile(join('./DISK', f))]
final_dict_files = [f for f in listdir('./DISK_FINAL') if isfile(join('./DISK_FINAL', f))]
# merging_files = [f for f in listdir('./output_no_number') if isfile(join('./output_no_number', f))]
backup_files = [f for f in listdir('./output_after_all_compressions') if
                isfile(join('./output_after_all_compressions', f))]
backup_files_copy = [f for f in listdir('./output_after_all_compressions_copy') if
                     isfile(join('./output_after_all_compressions_copy', f))]

merging_test = [f for f in listdir('./output_test') if isfile(join('./output_test', f))]


def spimi(reuters_files, block_files, block_files_dir, output_dir_final_dict):
    tokenize_all(reuters_files=reuters_files, output_dir=block_files_dir)
    read_all_files_at_once_and_make_final_dict(blocks_produced_from_tokenization=block_files,
                                               input_dir=block_files_dir, output_dir=output_dir_final_dict)


# spimi(files, disk_files, './DISK/', './DISK_FINAL/')
# merge_blocks(backup_files, './output_after_all_compressions/')

# read_all_files_at_once(backup_files)

# final_dict_files = [f for f in listdir('./final_dict') if isfile(join('./final_dict', f))]
# search_final_dict_or_query(query="jimmy carter", files=final_dict_files, files_dir='./final_dict/',
#                            query_type='or')

# merge_by_block_size(backup_files)


# final test

# tokenize_all(files=files, output_dir='./DISK/')
# merge_blocks(backup_files, './DISK/')
# read_all_files_at_once_and_make_final_dict(files=disk_files, input_dir='./DISK/', output_dir='./DISK_FINAL/')

search_final_dict(query="Jimmy Carter", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='or')

search_final_dict(query="Jimmy Carter", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="Green Party", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="Innovations in telecommunication", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='and')

search_final_dict(query="environmentalist ecologist", files=final_dict_files,
                  files_dir='./DISK_FINAL/',
                  query_type='or')

search_final_dict(query="Innovation in telecommunications", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='or')

search_final_dict(query="usa", files=final_dict_files, files_dir='./DISK_FINAL/',
                  query_type='')
