import re
import json
from multiprocessing.dummy import Pool as ThreadPool
from os import listdir
from os.path import isfile, join

from bs4 import BeautifulSoup

import nltk

nltk.download('punkt')


def mergeBlocks(files):
    # files = [f for f in listdir('./files') if isfile(join('./files', f))]
    word_counter = 0
    pattern = re.compile('\[\".*\",')
    words = open("words.txt", "w+")
    dict_from_text = {}
    word = ""
    id_list = ""
    for file in files:
        with open('./output_test/' + file) as fp:
            print(file)
            write_word = False
            write_id = False
            id_list = ""
            for line in fp:
                for ch in line:
                    if ch is "\"" and write_word is False:
                        if dict_from_text is not None and word in dict_from_text.keys() and id_list is not "":
                            dict_from_text[word] = dict_from_text[word].join(',' + id_list)
                        word = ""
                        word += ch
                        # if reaching 25 000, write dict to disk

                        write_word = True
                        # print(id_list)
                        # print("\n")
                        id_list = ""

                    elif write_word is True and ch is not "\"":
                        word += ch
                    # this is the end quotation mark of a word
                    elif write_word is True and ch is "\"":
                        write_word = False
                        word += ch
                        words.write(word)
                        words.write('\n')
                        if word not in dict_from_text.keys():
                            dict_from_text[word] = ""
                        word_counter += 1
                    # get the list of ID for that word, remove all the brackets
                    elif write_word is False and word is not "" and ch is not "[" and ch is not "]":
                        id_list += ch

    if dict_from_text is not None and word in dict_from_text.keys():
        dict_from_text[word] = dict_from_text[word].join(id_list)
    print(id_list)
    print(word_counter)
    print(len(dict_from_text.keys()))
    words.close()

    for key, value in dict_from_text.items():
        print(key)
        print("values: " + value)
        print('\n')


def clean_list(string_of_ids):
    list_of_ids = []
    for each in string_of_ids.split(','):
        list_of_ids.append(each)
    return list_of_ids


def tokenize(files):
    tuples = list()
    final_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0
    wrote_to_disk = False

    for file in files:
        with open('./files/' + file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            text = nltk.word_tokenize(soup.get_text())

            # go through data, add tokens to dictionary. Count article number. write to disk every 500
            for word in text:
                if word is "\x03":
                    newid += 1
                    wrote_to_disk = False
                final_dict = add_to_dict(word=word, newid=newid, my_dict=final_dict)

                if newid % 500 is 1 and newid is not 1 and not wrote_to_disk:
                    print(newid)
                    wrote_to_disk = True
                    disk_write = open("./output/block" + str(block_write) + ".txt", "w+")
                    disk_write.write(json.dumps(sorted(final_dict.items()), separators=(',', ':')))
                    disk_write.close()
                    block_write += 1
                    final_dict = {}
    if len(final_dict) is not 0:
        disk_write = open("./output/block" + str(block_write) + ".txt", "w+")
        disk_write.write(json.dumps(final_dict))
        disk_write.close()


def add_to_dict(word, newid, my_dict):
    if word not in my_dict.keys():
        my_dict[word] = [newid]
    else:
        if newid not in my_dict[word]:
            # if value doesn't exist in value list for given key
            my_dict[word].append(newid)
    return my_dict


def tokenize_sgm(article, soup_obj):
    tuples = []
    if soup_obj.find(newid=article['newid']) is not None:
        # assign it to the key newid
        body = soup_obj.find(newid=article['newid']).getText()
        body = nltk.word_tokenize(body)
        tuples.extend(make_tuples(body, article['newid']))
        for tuple in tuples:
            print(tuple)
    return tuples


def tokenize_sgm_articles(articles, soup_obj):
    tuples = []
    pool = ThreadPool(80)
    for article in articles:
        tuples.append(pool.apply_async(tokenize_sgm, (article, soup_obj)))
    pool.close()
    pool.join()
    return tuples


def make_tuples(body, newid):
    tuples_list = []
    for word in body:
        tuples_list.append(tuple((word, newid)))
    return tuples_list


def spimi_invert(token_stream):
    article_counter = 0
    dict_block = {}
    file = open('block' + str(article_counter) + '.txt', 'w+')

    if article_counter % 500 is 0:
        file = open('block' + str(article_counter) + '.txt', 'w+')
        article_counter += 1
        dict_block = {}

    for token in token_stream.items():
        if token not in dict_block.keys():
            dict_block[token] = token_stream[token]
        else:
            if token_stream[token] not in dict_block[token].values():
                dict_block[token_stream].append(token_stream[token])
    for key, value in sorted(dict_block.items()):
        file.write(key + ': ')
        id_list_str = ''
        for each_id in value:
            id_list_str += each_id + ', '
        file.write(id_list_str)
        file.write('\n')
    return file.name
