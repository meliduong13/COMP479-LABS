import json
import re

import jsbeautifier
import contextlib

opts = jsbeautifier.default_options()
from bs4 import BeautifulSoup

import nltk

nltk.download('punkt')
from nltk.corpus import stopwords

nltk.download("stopwords")
opts.indent_size = 0


def read_all_files_at_once(files):
    dict_filename_prefix = 'final'
    dict_block_number = 0
    read_limit = 0
    with contextlib.ExitStack() as stack:
        fp_list = [stack.enter_context(open('./output_after_all_compressions/' + fname)) for fname in files]
        done_reading = 0
        print(len(fp_list))
        keep_looping = True
        dict_block = {}
        while keep_looping:
            for fp in fp_list:
                line_read = fp.readline()

                term = re.findall(r'"(.*?)"', line_read)
                values = re.findall(r'": \[(.*?)\]', line_read)

                if term is not None and len(term) is not 0:
                    term = term[0]
                if values is not None and len(values) is not 0:
                    values = values[0].replace(" ", "")
                    values = values.split(',')
                    try:
                        values = list(map(int, values))
                    except:
                        print('error:'+values)
                    result = add_to_dict_array(key=term, values=values, my_dict=dict_block)
                    dict_block = result[0]
                    is_new_term = result[1]
                    if is_new_term is True:
                        read_limit += 1
                # if the term added
                if read_limit % 25000 == 0 and read_limit is not 0:
                    print('number of terms so far: ' + str(read_limit))
                    dict_block_number += 1
                    disk_write = open(
                        "./final_dict/" + str(dict_filename_prefix) + str(
                            dict_block_number) + ".txt", "w+")
                    disk_write.write(jsbeautifier.beautify(json.dumps(dict_block, sort_keys=True)))
                    disk_write.close()
                    dict_block = {}
                if line_read is "}":
                    done_reading += 1
                    if done_reading is len(fp_list):
                        keep_looping = False

    if len(dict_block) is not 0:
        print('remaining terms printed in last block')
        dict_block_number += 1
        disk_write = open(
            "./final_dict/" + str(dict_filename_prefix) + str(
                dict_block_number) + ".txt", "w+")
        disk_write.write(jsbeautifier.beautify(json.dumps(dict_block, sort_keys=True)))
        disk_write.close()


def get_list_top_30_words():
    top_30_words_list = []

    with open('top_30_words_backup.txt') as fp:
        for line in fp:
            if line is not "":
                line = line.strip('\n')
                top_30_words_list.append(line)
    fp.close()
    i = 0
    for each in top_30_words_list:
        i += 1
        print(each + str(i))
    return top_30_words_list


def get_list_top_150_words():
    top_150_words_list = []

    with open('top_150_words_backup.txt') as fp:
        for line in fp:
            if line is not "":
                line = line.strip('\n')
                top_150_words_list.append(line)
    fp.close()
    i = 0
    for each in top_150_words_list:
        i += 1
        print(str(i) + each)
    return top_150_words_list


def merge_blocks(files, dir):
    dict_file = open("words2.txt", "w+")
    dict_from_text = {}
    for file in files:
        with open(dir + file) as fp:
            print(file)
            line_counter = 0
            for line in fp:
                line_counter += 1
                line_as_string = line
                term = re.findall(r'"(.*?)"', line_as_string)
                values = re.findall(r'": \[(.*?)\]', line_as_string)

                if term is not None and len(term) is not 0:
                    if term[0] not in dict_from_text.keys():
                        dict_from_text[term[0]] = []
                if values is not None and len(values) is not 0:
                    values = values[0].replace(" ", "")
                    values = values.split(',')
                    try:
                        values_as_int_list = list(map(int, values))
                        dict_from_text[term[0]].extend(values_as_int_list)
                    except:
                        print(values_as_int_list)
    # sort_by_values_len_top_words(dict_from_text)
    dict_file.write(jsbeautifier.beautify(json.dumps(dict_from_text, sort_keys=True)))
    dict_file.close()
    print('done writing my whole dicionary!')
    total = 0
    for key, value in dict_from_text.items():
        total += len(value)
    print('total length of values' + str(total))


def add_to_dict_array(key, values, my_dict):
    is_new_term = True
    if key not in my_dict.keys():
        my_dict[key] = values
        is_new_term = True

    else:
        if values not in my_dict[key]:
            # if value doesn't exist in value list for given key
            my_dict[key] += values
        if key in my_dict.keys():
            is_new_term = False
    return my_dict, is_new_term


def add_to_dict(key, value, my_dict):
    if key not in my_dict.keys():
        my_dict[key] = [value]
    else:
        if value not in my_dict[key]:
            # if value doesn't exist in value list for given key
            my_dict[key].append(value)
    return my_dict


def tokenize_all(files):
    top30 = stopwords.words('english')[0:30]
    top150 = stopwords.words('english')[0:150]
    tuples = list()
    final_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0
    total_terms = 0

    for file in files:
        with open('./files/' + file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            text = soup.get_text()
            text = ''.join(each for each in text if not each.isdigit())
            text = text.lower()
            text = nltk.word_tokenize(text)
            # if token is not in top 150
            text = [each for each in text if each not in top150]
            total_terms += len(text)

            # go through data, add tokens to dictionary. Count article number. write to disk every 500
            for word in text:
                if word is "\x03":
                    newid += 1
                    wrote_to_disk = False
                # if writing to new block, write all previously added items to dictionary
                if newid % 500 is 1 and newid is not 1 and not wrote_to_disk:
                    print(newid)
                    wrote_to_disk = True

                    if len(str(block_write)) is 1:
                        print('if')
                        disk_write = open("./output_no_number/block0" + str(block_write) + ".txt", "w+")
                    else:
                        print('else')
                        disk_write = open("./output_no_number/block" + str(block_write) + ".txt", "w+")
                    # write all previous data to file
                    if word is "\x03":
                        print('heyyy')
                        print(newid)
                        final_dict = add_to_dict(key=word, value=newid - 1, my_dict=final_dict)
                    else:
                        # never used
                        print('ahhhhhhhhhhhhhhhhhhh')
                        final_dict = add_to_dict(key=word, value=newid, my_dict=final_dict)
                    disk_write.write(jsbeautifier.beautify(json.dumps(final_dict, sort_keys=True)))
                    disk_write.close()

                    # increment block number
                    block_write += 1
                    # reset dictionary
                    final_dict = {}

                # if not starting a new block, just add to dict
                else:
                    if word is "\x03":
                        final_dict = add_to_dict(key=word, value=newid - 1, my_dict=final_dict)
                    else:
                        final_dict = add_to_dict(key=word, value=newid, my_dict=final_dict)
    # remaining that has not been written to disk
    if len(final_dict) is not 0:
        print('last block')
        print(block_write)
        if len(str(block_write)) is 1:
            print('if')
            disk_write = open("./output_no_number/block0" + str(block_write) + ".txt", "w+")
        else:
            print('else')
            disk_write = open("./output_no_number/block" + str(block_write) + ".txt", "w+")
        disk_write.write(jsbeautifier.beautify(json.dumps(final_dict, sort_keys=True)))
        disk_write.close()
    print('total terms' + str(total_terms))
