import ast
import contextlib
import json
import re

import jsbeautifier
import math

opts = jsbeautifier.default_options()
from bs4 import BeautifulSoup

import nltk

nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")
opts.indent_size = 0


# this method is used to sort dictionary items by length of their value
# the value of the dictionary contains a list of items
def sort_by_values_len(my_dict):
    dict_len = {key: len(value) for key, value in my_dict.items()}
    import operator
    sorted_key_list = sorted(dict_len.items(), key=operator.itemgetter(1), reverse=True)
    sorted_dict = [{item[0]: my_dict[item[0]]} for item in sorted_key_list]
    return sorted_dict


def make_list_from_dict_values(dict_values_list):
    new_list = []
    for each in dict_values_list:
        new_list.append(each[0])
    return new_list


# the final dictionary spreads over 4 files in the directory 'DISK_FINAL'
# this method searches from those files for an 'AND' or 'OR' query
# to do that it reads each file, line by line, retrieves the key and values per line
# then verifies whether the searched words in the query are contained in the dictionary
# if they are, the values of the list of ids is retrieved
def search_final_dict(query, files, files_dir, query_type):
    user_search = query
    query_type = query_type
    query = ''.join(each for each in query if not each.isdigit())
    top150 = stopwords.words('english')[0:150]
    keywords_dict = {}
    query = query.split()
    # prepare the dictionary keys based on the query
    for each in query:
        each = each.lower()
        if each not in top150:
            keywords_dict[each] = []

        # open the appropriate file depending on the word
        if each <= 'bra':
            file = 'final_1.txt'
        elif 'bra' < each < 'montagne':
            file = 'final_2.txt'
        else:
            file = 'final_3.txt'

        with open(files_dir + file) as fp:
            for line in fp:

                term = re.findall(r'"(.*?)" :', line)
                # if the term exists
                if term is not None and len(term) is not 0:
                    term = term[0]
                    # if the keyword is equal to the dictionary term
                    if term in keywords_dict.keys():
                        # get values and add to the keywords dict
                        try:
                            values_list = line[line.index('\" :[') + 3:]
                            if values_list is not None and len(values_list) is not 0:
                                values_list = ast.literal_eval(values_list)
                                keywords_dict[term] = values_list
                                print(values_list)
                                break
                        except:
                            print('error:' + values_list)

    if len(keywords_dict) is 1:
        print('\nResults for the single word query ' + "\"" + user_search + "\"")
        print('\n' + jsbeautifier.beautify(json.dumps(keywords_dict, sort_keys=True)))
    elif query_type is 'and':
        print('\nResults for the "and" query ' + "\"" + user_search + "\"")
        print('\n' + jsbeautifier.beautify(json.dumps(keywords_dict, sort_keys=True)))
        doc_ids = []
        for each in keywords_dict.values():
            doc_ids.append(make_list_from_dict_values(each))
        doc_ids = sorted(set.intersection(*map(set, doc_ids)))
        print(doc_ids)
        calculate_doc_score(doc_id_list=doc_ids, dictionary=keywords_dict, k1=2, b=0.5)
    elif query_type is 'or':
        print('\nResults with keywords contained in each article for the "or" query ' + "\"" + user_search + "\"")
        print('\n' + jsbeautifier.beautify(json.dumps(keywords_dict, sort_keys=True)))
        doc_ids = []
        for each in keywords_dict.values():
            doc_ids.append(make_list_from_dict_values(each))
        doc_ids = sorte(set.union())

        # for each in
        # list_of_or_query = sorted(set.union(*map(set, (keywords_dict.values()))))
        #
        # dict_or_query = {}
        # for each_id in list_of_or_query:
        #     for word, doc_id_list in keywords_dict.items():
        #         if each_id in doc_id_list:
        #             if each_id not in dict_or_query:
        #                 dict_or_query[each_id] = [word]
        #             else:
        #                 dict_or_query[each_id] += [word]
        # sorted_by_frequency_of_keys = sort_by_values_len(dict_or_query)
        # # print(jsbeautifier.beautify(json.dumps(sort_by_values_len(dict_or_query), sort_keys=True)))
        # for each in sorted_by_frequency_of_keys:
        #     print(each)
        #
        # all_keys = []
        # for each in sorted_by_frequency_of_keys:
        #     all_keys += each.keys()
        # print('\nResults in a list format for the "or" query ' + "\"" + user_search + "\"")
        # print(
        #     'All results are in order of frequency. Articles at the beginning of the list contain the most keywords. '
        #     'Articles at the end of the list contain the least.')
        # print(all_keys)


def calculate_doc_score(doc_id_list, dictionary, k1, b):
    num_docs = 21578
    l_avg = 118
    k1 = k1
    b = b
    score_dict = {}
    for doc_id in doc_id_list:
        for word in dictionary.keys():
            doc_freq_of_term = len(dictionary[word])
            for word_and_freq in dictionary[word]:
                if word_and_freq[0] == doc_id:
                    print('*********')
                    print('calculating the score for doc ' + str(doc_id))
                    term_freq_in_doc = word_and_freq[1]
                    # getting the doc length for given word
                    with open('DOC_LENGTH_DICT.txt') as fp:
                        print('opened doc')
                        try:
                            for i, line in enumerate(fp):
                                if i == doc_id + 1:
                                    print('found line')
                                    doc_len = line[line.index('\": ') + 3:]
                                    doc_len = doc_len.replace(",", "")
                                    doc_len = doc_len.replace(" ", "")
                                    doc_len = doc_len.replace("\\n", "")
                                    doc_len = int(doc_len)
                                    score = math.log10(num_docs / doc_freq_of_term) * ((k1 + 1) * term_freq_in_doc) / (
                                            k1 * (1 - b) + b * (doc_len / l_avg) + term_freq_in_doc)
                                    if doc_id not in score_dict.keys():
                                        score_dict[doc_id] = score
                                    else:
                                        score_dict[doc_id] += score

                                    print('score for doc ' + str(doc_id) + ' for word ' + word)
                        except ValueError:
                            print('cannot convert value to int')
    print(jsbeautifier.beautify(json.dumps(score_dict, sort_keys=True)))
    return score_dict


def read_files_and_write(blocks_produced_from_tokenization, input_dir, output_dir):
    dict_filename_prefix = 'final'
    dict_block_number = 0
    read_limit = 0
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    with contextlib.ExitStack() as stack:
        fp_list = [stack.enter_context(open(input_dir + fname)) for fname in blocks_produced_from_tokenization]
        done_reading = 0
        print(len(fp_list))
        keep_looping = True
        dict_block = {}
        line_num = 0
        while keep_looping:
            line_num += 1
            for fp in fp_list:
                line_read = fp.readline()
                if line_read is "":
                    print('nothing')
                elif 'EOF' in line_read:
                    done_reading += 1
                    if done_reading is len(fp_list):
                        keep_looping = False
                else:
                    term = re.findall(r'"(.*?)" :', line_read)
                    if term is not None and len(term) is not 0:
                        term = term[0]
                    try:
                        values_list = line_read[line_read.index('\" :[') + 3:]
                        if values_list is not None and len(values_list) is not 0:
                            values_list = ast.literal_eval(values_list)
                            if term <= 'bra':
                                print('bra')
                                dict_1 = add_to_positional_dict_with_array(term=term, doc_id_freq_array=values_list,
                                                                           my_dict=dict_1)
                            elif 'bra' < term < 'montagne':
                                print('mont.')
                                dict_2 = add_to_positional_dict_with_array(term=term, doc_id_freq_array=values_list,
                                                                           my_dict=dict_2)
                            else:
                                print('last')
                                dict_3 = add_to_positional_dict_with_array(term=term, doc_id_freq_array=values_list,
                                                                           my_dict=dict_3)
                    except Exception as e:
                        print(e)

                        print('content: ' + line_read)
                        print(line_read)
                        print(fp)
                        print(term)
                        print(line_read)
                        quit()

    print(len(dict_1))
    print(len(dict_2))
    print(len(dict_3))

    with open(output_dir + dict_filename_prefix + str('_1') + ".txt", 'w+') as disk_write:
        [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
         sorted(dict_1.items())]
        disk_write.write('EOF')
        disk_write.close()

    with open(output_dir + dict_filename_prefix + str('_2') + ".txt", 'w+') as disk_write:
        [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
         sorted(dict_2.items())]
        disk_write.write('EOF')
        disk_write.close()

    with open(output_dir + dict_filename_prefix + str('_3') + ".txt", 'w+') as disk_write:
        [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
         sorted(dict_3.items())]
        disk_write.write('EOF')
        disk_write.close()


# this method reads from the 44 blocks of dictionary that were first produced
#  each dictionary block is distributed in one of the 44 files in the directory 'DISK'
# it then opens up the 44 files, had a file parser point to each of the files
# each of the 44 lines are read one after the other, where each line is from 1 of the 44 different files
# after 25000 unique terms are found, a dictionary made of those 25000 terms is written into a file in the directory
# 'DISK_FINAL'
# that dicitonary is erased, then the next 25000 terms are read, written to a file, and so on
def read_all_files_at_once_and_make_final_dict(blocks_produced_from_tokenization, input_dir, output_dir):
    dict_filename_prefix = 'final'
    dict_block_number = 0
    read_limit = 0
    with contextlib.ExitStack() as stack:
        fp_list = [stack.enter_context(open(input_dir + fname)) for fname in blocks_produced_from_tokenization]
        done_reading = 0
        print(len(fp_list))
        keep_looping = True
        dict_block = {}
        while keep_looping:
            for fp in fp_list:
                line_read = fp.readline()

                term = re.findall(r'"(.*?)":', line_read)
                values = re.findall(r'": \[(.*?)\]', line_read)

                if term is not None and len(term) is not 0:
                    term = term[0]
                if values is not None and len(values) is not 0:
                    values = values[0].replace(" ", "")
                    values = values.split(',')
                    try:
                        values = list(map(int, values))
                    except:
                        print('error:' + values)
                    result = add_to_dict_array(key=term, values=values, my_dict=dict_block)
                    dict_block = result[0]
                    is_new_term = result[1]
                    if is_new_term is True:
                        read_limit += 1
                # if the term added
                if read_limit % 25000 == 0 and read_limit is not 0:
                    print('number of terms processed so far: ' + str(read_limit))
                    dict_block_number += 1
                    disk_write = open(
                        output_dir + str(dict_filename_prefix) + str(
                            dict_block_number) + ".txt", "w+")
                    disk_write.write(jsbeautifier.beautify(json.dumps(dict_block, sort_keys=True)))
                    disk_write.close()
                    dict_block = {}
                if line_read is "}":
                    done_reading += 1
                    if done_reading is len(fp_list):
                        keep_looping = False

    if len(dict_block) is not 0:
        print('remaining terms processed in last block')
        dict_block_number += 1
        disk_write = open(
            output_dir + str(dict_filename_prefix) + str(
                dict_block_number) + ".txt", "w+")
        disk_write.write(jsbeautifier.beautify(json.dumps(dict_block, sort_keys=True)))
        disk_write.close()


# this method is used to generate the final dictionary into a single file
# it reads the 44 blocks in the direcotry 'DISK', where each 500 reuters articles is written to dictionary into a
# single file, and merges those 44 blocks into a single dictionary
# it is NOT used for the SPIMI algorithm
# It's only purpose is to help generate the table based on the book's table 5.1
# it is used to retrieve the number of unique terms the dictionary contains depending on the compression technique used
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
                values = re.findall(r'\[(.*?)\]', line_as_string)

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


# small helper method to write a word and newid to dictionary
# it returns the dictionary with newly added terms and/or newid value
# it also returns a boolean to indicate whether the word added to dictionary already exists or not
# if the word already exists in the dictionary, return false
# if the word doesn't exist in the dictionary, return true
def add_to_dict_array(key, values, my_dict):
    is_new_term = True
    try:
        if key not in my_dict.keys():
            my_dict[key] = values
            is_new_term = True

        else:
            if values not in my_dict[key]:
                # if value doesn't exist in value list for given key
                my_dict[key] += values
                my_dict[key].sort()
            if key in my_dict.keys():
                is_new_term = False
    except Exception as e:
        print('error')
        print(e)
        print('key')
        print(key)
        print('value')
        print(values)
    return my_dict, is_new_term


def add_to_block(key, values, my_dict):
    try:
        if key not in my_dict.keys():
            my_dict[key] = values
        else:
            if values not in my_dict[key]:
                # if value doesn't exist in value list for given key
                my_dict[key] += values
                my_dict[key].sort()
    except Exception as e:
        print('error')
        print(e)
        print('key')
        print(key)
        print('value')
        print(values)
    return my_dict


# small helper method used to write a word and newid to dicionary
#  it is used to generate 44 dictionary blocks
# key is the word
# value is doc_id
def add_to_positional_dict(term, doc_id, my_dict):
    found_doc_id = False
    if term not in my_dict.keys():
        my_dict[term] = [[doc_id, 1]]
    else:
        # if doc_id exists already in value list, increment its frequency
        for id_freq in my_dict[term]:
            if id_freq[0] is doc_id:
                id_freq[1] += 1
                found_doc_id = True
        #  if doc_id doesn't exist for given term, append it to the existing list with frequency 1
        if found_doc_id is False:
            my_dict[term].append([doc_id, 1])
    return my_dict


def add_to_positional_dict_with_array(term, doc_id_freq_array, my_dict):
    found_doc_id = False
    for doc_id_freq_input in doc_id_freq_array:
        try:
            if term not in my_dict.keys():
                my_dict[term] = [doc_id_freq_input]
            else:
                # if doc_id exists already in value list, increment its frequency
                for each in my_dict[term]:
                    # if the newly added values 'each' have the doc_id in the dictionary, increment the frequency to
                    # that
                    # of 'each'
                    if each[0] is doc_id_freq_input[0]:
                        each[1] += doc_id_freq_input[1]
                        found_doc_id = True
                #  if doc_id doesn't exist for given term, append it to the existing list with frequency 1
                if found_doc_id is False:
                    my_dict[term].append(doc_id_freq_input)

        except TypeError as e:
            print(e)
            print(term)
            print(doc_id_freq_input)
    print('added term:' + term)
    return my_dict


# small helper method used to write a owrd and newid to dicionary
#  it is used to generate 44 dictionary blocks
def add_to_dict(key, value, my_dict):
    if key not in my_dict.keys():
        my_dict[key] = [value]
    else:
        if value not in my_dict[key]:
            # if value doesn't exist in value list for given key
            my_dict[key].append(value)
    return my_dict


# first step in the SPIMI algorithm
# the reuters files are tokenized and written to 44 different dictionaries, where every dictionary is written to a file
# and each 500 reuters article parsed is written to a dictionary
# the tokenization uses a combinaison lossy dictionary compression techniques
# the techniques used are the ones generated in the report's table:
# removal of numbers
# case folding
# removal of 150 stop words provided by the nltk library
# porter stemming (only used for table 5.1 not for the dictionary used for the queries
def tokenize_all(reuters_files, output_dir):
    top30 = stopwords.words('english')[0:30]
    top150 = stopwords.words('english')[0:150]
    final_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0
    total_terms = 0
    ps = PorterStemmer()
    terms_dict = {}
    # todo create a dict containing key=docID, value=doc length
    doc_length_dict = {}
    doc_length_avg = 0
    print('starting to write a dictionary every 500 reuters articles...')
    for file in reuters_files:
        with open('./files/' + file) as fp:
            doc_length = 0
            soup = BeautifulSoup(fp, 'html.parser')
            text = soup.get_text()
            text = ''.join(each for each in text if not each.isdigit())
            text = text.lower()
            text = nltk.word_tokenize(text)
            # if token is not in top 150
            text = [each for each in text if each not in top150]

            # use of porter stemmer for the table 5.1 but not for the final dictionary that was queried
            # text = [ps.stem(each) for each in text]
            total_terms += len(text)

            # each word becomes a token in a dictionary. Every 500 terms, write those to disk
            for word in text:
                doc_length += 1
                # put all terms in a separate dictionary in order to delimitate the first word in the 25k words per
                # block
                terms_dict = add_to_positional_dict(term=word, doc_id=None, my_dict=terms_dict)
                # this word signals the end of an article
                if word is "\x03":
                    # doc_length += 1
                    newid += 1
                    doc_length_dict[newid - 1] = doc_length
                    # when reaching the end of a document, increment the document's length, which will be divided at
                    # the end to give the doc length average
                    doc_length_avg += doc_length
                    doc_length = 0
                    wrote_to_disk = False
                # if writing to new block, write all previously added items to dictionary
                if newid % 500 is 1 and newid is not 1 and not wrote_to_disk:
                    print('reached article ' + str(newid))
                    wrote_to_disk = True

                    if word is "\x03":
                        print('reached article ' + str(newid))
                        final_dict = add_to_positional_dict(term=word, doc_id=newid - 1, my_dict=final_dict)
                    else:
                        final_dict = add_to_positional_dict(term=word, doc_id=newid, my_dict=final_dict)

                    if len(str(block_write)) is 1:
                        block_prefix = "BLOCK0"
                    else:
                        block_prefix = "BLOCK"

                    with open(output_dir + block_prefix + str(block_write) + ".txt", 'w+') as disk_write:
                        [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in
                         sorted(final_dict.items())]
                        disk_write.write('EOF')

                    # increment block number
                    block_write += 1
                    # reset dictionary
                    final_dict = {}

                # if not starting a new block, just add to dict
                else:
                    if word is "\x03":
                        final_dict = add_to_positional_dict(term=word, doc_id=newid - 1, my_dict=final_dict, )
                    else:
                        final_dict = add_to_positional_dict(term=word, doc_id=newid, my_dict=final_dict)
    # remaining that has not been written to disk is written to the last block
    if len(final_dict) is not 0:
        print('last block to write with remaining terms')
        print(block_write)
        if len(str(block_write)) is 1:
            block_prefix = "BLOCK0"
        else:
            block_prefix = "BLOCK"

        with open(output_dir + block_prefix + str(block_write) + ".txt", 'w+') as disk_write:
            [disk_write.write('"{0}" :{1}\n'.format(key, value)) for key, value in sorted(final_dict.items())]
            disk_write.write('EOF')
        disk_write.close()
    print('total number of terms ' + str(total_terms))
    terms_ordered = []
    for i in sorted(terms_dict.keys()):
        terms_ordered.append(i)

    print(len(terms_ordered))
    print('first block value' + terms_ordered[0])
    print('first block value' + terms_ordered[25000])
    print('first block value' + terms_ordered[50000])
    disk_write = open("test.txt", "w+")
    for each in terms_ordered:
        disk_write.write(each)
        disk_write.write('\n')
    disk_write.close()

    doc_length_avg = doc_length_avg / len(doc_length_dict)
    print('doc length average ' + str(doc_length_avg))
    disk_write = open("DOC_LENGTH_DICT" + ".txt", "w+")
    disk_write.write(jsbeautifier.beautify(json.dumps(doc_length_dict, sort_keys=True)))
    disk_write.close()
