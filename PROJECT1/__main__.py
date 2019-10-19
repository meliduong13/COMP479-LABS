from os import listdir
from os.path import isfile, join

from spimi import *

bloc_counter = 0
files = [f for f in listdir('./files') if isfile(join('./files', f))]
merging_files = [f for f in listdir('./output_no_number') if isfile(join('./output_no_number', f))]

# tokenize_all(files)
# time.sleep(15)

merging_test = [f for f in listdir('./output_test') if isfile(join('./output_test', f))]
# mergeBlocks(merging_files)
merge_blocks(merging_files, './output_no_number/')

# from nltk.corpus import stopwords
# nltk.download("stopwords")
# print(len(stopwords.words('english')[0:30]))
# # line = "i am yours and that is really it."
# top30 = stopwords.words('english')[0:30]
# line = [each for each in line if each not in top30]
# print(line)
# for each in top30:
# print(each)