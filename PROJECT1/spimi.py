import re
import json
from multiprocessing.dummy import Pool as ThreadPool
from os import listdir
from os.path import isfile, join
import jsbeautifier
import time
import ast

opts = jsbeautifier.default_options()
from bs4 import BeautifulSoup

import nltk

nltk.download('punkt')

opts.indent_size = 0


def sort_by_values_len_top_words(dict, num_top_words):
    sorted_items = sorted(dict.items(), key=lambda item: len(item[1]), reverse=True)
    counter = 0
    top_words = []
    for key, value in sorted_items:
        if counter < num_top_words + 1:
            print(key)
            return top_words
        counter += 1


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
    dict_file.write(jsbeautifier.beautify(json.dumps(dict_from_text, sort_keys=True)))
    dict_file.close()
    print('done writing my whole dicionary!')


def mergeBlocks(files):
    # files = [f for f in listdir('./files') if isfile(join('./files', f))]
    word_counter = 0
    words = open("words.txt", "w+")
    dict_from_text = {}
    word = ""
    id_list = ""
    for file in files:
        with open('./output/' + file) as fp:
            print(file)
            write_word = False
            write_id = False
            id_list = ""
            for line in fp:
                for ch in line:
                    if ch is "\"" and write_word is False:
                        if dict_from_text is not None and word in dict_from_text.keys() and id_list is not "":
                            dict_from_text[word].append(id_list)
                        word = ""
                        word += ch
                        # if reaching 25 000, write dict to disk

                        write_word = True
                        # words.write(id_list)
                        words.write('\n')
                        # print("\n")
                        id_list = ""

                    elif write_word is True and ch is not "\"":
                        word += ch
                    # this is the end quotation mark of a word
                    elif write_word is True and ch is "\"":
                        write_word = False
                        word += ch
                        if word not in dict_from_text.keys():
                            words.write(word)
                            words.write('\n')
                        if word not in dict_from_text.keys():
                            dict_from_text[word] = []
                        word_counter += 1
                    # get the list of ID for that word, remove all the brackets
                    elif write_word is False and word is not "" and ch is not "[" and ch is not "]":
                        id_list += ch
            if dict_from_text is not None and word in dict_from_text.keys() and id_list is not "":
                dict_from_text[word].append(id_list)
    print(id_list)
    print(word_counter)
    print(len(dict_from_text.keys()))
    words.close()

    dict_file = open("dict.txt", "w+")
    for key, value in dict_from_text.items():
        dict_file.write(key + ': ')
        id_list_str = ''
        for each_id in value:
            id_list_str += each_id + ', '
        dict_file.write(id_list_str)
        dict_file.write('\n')
    dict_file.close()


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
            # text = re.sub(r'[0-9]+', '', text)

            # go through data, add tokens to dictionary. Count article number. write to disk every 500
            for word in text:
                if word is "\x03":
                    wrote_to_disk = False
                    final_dict = add_to_dict_if_not_number(word=word, newid=newid, my_dict=final_dict)
                    newid += 1

                if newid % 500 is 0 and not wrote_to_disk:
                    print(newid)
                    wrote_to_disk = True
                    if len(str(block_write)) is 1:
                        print('if')
                        disk_write = open("./output_no_number/block0" + str(block_write) + ".txt", "w+")
                    else:
                        print('else')
                        disk_write = open("./output_no_number/block" + str(block_write) + ".txt", "w+")
                    disk_write.write(jsbeautifier.beautify(json.dumps(final_dict, sort_keys=True)))
                    disk_write.close()
                    block_write += 1
                    final_dict = {}
    if len(final_dict) is not 0:
        print('in here')
        print(len(final_dict))
        disk_write = open("./output_no_number/block" + str(block_write) + ".txt", "w+")
        disk_write.write(jsbeautifier.beautify(json.dumps(final_dict, sort_keys=True)))
        disk_write.close()


def add_to_dict(word, newid, my_dict):
    if word not in my_dict.keys():
        my_dict[word] = [newid]
    else:
        if newid not in my_dict[word]:
            # if value doesn't exist in value list for given key
            my_dict[word].append(newid)
    return my_dict


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        int(s.replace(',', ''))
        return True
    except ValueError:
        pass
    try:
        time.strptime(s, '%H:%M:%S.%f')
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def add_to_dict_if_not_number(word, newid, my_dict):
    if is_number(word):
        return my_dict
    if word not in my_dict.keys():
        my_dict[word] = [newid]
    else:
        if newid not in my_dict[word]:
            # if value doesn't exist in value list for given key
            my_dict[word].append(newid)
    return my_dict


def add_to_dict_and_remove_case(word, newid, my_dict):
    word = word.lower()
    if word not in my_dict.keys():
        my_dict[word] = [newid]
    else:
        if newid not in my_dict[word]:
            # if value doesn't exist in value list for given key
            my_dict[word].append(newid)
    return my_dict


def tokenize_all(files):
    tuples = list()
    final_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0

    for file in files:
        with open('./files/' + file) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            text = soup.get_text()
            text = ''.join(each for each in text if not each.isdigit())
            text = text.lower()
            text = nltk.word_tokenize(text)
            # TODO case folding

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
                        final_dict = add_to_dict(word=word, newid=newid - 1, my_dict=final_dict)
                    else:
                        # never used
                        print('ahhhhhhhhhhhhhhhhhhh')
                        final_dict = add_to_dict(word=word, newid=newid, my_dict=final_dict)
                    disk_write.write(jsbeautifier.beautify(json.dumps(final_dict, sort_keys=True)))
                    disk_write.close()

                    # increment block number
                    block_write += 1
                    # reset dictionary
                    final_dict = {}

                # if not starting a new block, just add to dict
                else:
                    if word is "\x03":
                        final_dict = add_to_dict(word=word, newid=newid - 1, my_dict=final_dict)
                    else:
                        final_dict = add_to_dict(word=word, newid=newid, my_dict=final_dict)
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
