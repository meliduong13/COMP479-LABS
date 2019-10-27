from os import listdir
from os.path import isfile, join

from spimi import *

bloc_counter = 0
files = [f for f in listdir('./files') if isfile(join('./files', f))]
# merging_files = [f for f in listdir('./output_no_number') if isfile(join('./output_no_number', f))]
backup_files = [f for f in listdir('./output_after_all_compressions') if isfile(join('./output_after_all_compressions', f))]
backup_files_copy = [f for f in listdir('./output_after_all_compressions_copy') if isfile(join('./output_after_all_compressions_copy', f))]
# merge_by_block_size(backup_files)
# tokenize_all(files)

merging_test = [f for f in listdir('./output_test') if isfile(join('./output_test', f))]

# merge_blocks(backup_files, './output_after_all_compressions/')
read_all_files_at_once(backup_files)



# from nltk.corpus import stopwords
# nltk.download("stopwords")
# print(len(stopwords.words('english')[0:30]))
# # line = "i am yours and that is really it."
# top30 = stopwords.words('english')[0:30]
# line = [each for each in line if each not in top30]
# print(line)
# for each in top30:
# print(each)
