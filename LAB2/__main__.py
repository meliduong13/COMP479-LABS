from os import listdir
from os.path import isfile, join

from LAB2.LAB2 import *

files = [f for f in listdir('./files/files_smaller') if isfile(join('./files/files_smaller', f))]
print(files)

inverted_index = populate_inverted_index_key('./all-places-strings.lc.txt')

for file in files:
    soup = get_soup_obj('./files/files_smaller/' + file)
    contents = get_all_articles_in_file(soup)
    newid_dict = make_dict_with_newid_and_each_article_content(contents, soup)
    inverted_index = populate_inverted_index(newid_dict, inverted_index)
print_inverted_index(inverted_index)
