import nltk
import string
import queue
from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
import json
import math

nltk.download('punkt')


def tokenize(files):
    tuples = list()
    final_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0

    for file in files:
        with open('./files/' + file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            text = nltk.word_tokenize(soup.get_text())

            # go through data, add tokens to dictionary. Count article number. write to disk every 500
            for word in text:
                if word is "\x03":
                    newid += 1
                    wrote_to_disk = False

                if newid % 500 is 0 and not wrote_to_disk:
                    print(newid)
                    wrote_to_disk = True
                    disk_write = open("./output/block" + str(block_write) + ".txt", "w+")
                    disk_write.write(json.dumps(final_dict))
                    disk_write.close()
                    block_write += 1
                    final_dict = {}
                    final_dict = add_to_dic(word=word, newid=newid, my_dict=final_dict)

                else:
                    final_dict = add_to_dic(word=word, newid=newid, my_dict=final_dict)
    # remaining that has not been written to disk
    if len(final_dict) is not 0:
        disk_write = open("./output/block" + str(block_write) + ".txt", "w+")
        disk_write.write(json.dumps(final_dict))
        disk_write.close()

def add_to_dic(word, newid, my_dict):
    if word not in my_dict.keys():
        my_dict[word] = [newid]
    else:
        if newid not in my_dict[word]:
            # if value doesn't exist in value list for given key
            my_dict[word].append(newid)
    return my_dict


# def write_to_disk()


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
