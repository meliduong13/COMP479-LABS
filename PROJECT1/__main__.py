from os import listdir
from os.path import isfile, join

from spimi import *

bloc_counter = 0
files = [f for f in listdir('./files') if isfile(join('./files', f))]
merging_files = [f for f in listdir('./output_no_number') if isfile(join('./output_no_number', f))]
tokenize_all(files)

merging_test = [f for f in listdir('./output_test') if isfile(join('./output_test', f))]
# mergeBlocks(merging_files)
merge_blocks(merging_files, './output_no_number/')

