import ast
import contextlib
import json
import re

import jsbeautifier
import math

from helpers import *

opts = jsbeautifier.default_options()
from bs4 import BeautifulSoup

import nltk

nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download("stopwords")
opts.indent_size = 0


# the final dictionary spreads over 3 files in the directory 'DISK_FINAL'
# this method searches from those files for an 'AND' or 'OR' query
# to do that it reads each file, line by line, retrieves the key and values per line
# then verifies whether the searched words in the query are contained in the frequency dictionary
# if they are, the values of the list of ids and frequency are retrieved
def search_final_dict(query, files_dir, query_type):
    ps = PorterStemmer()
    user_search = query
    query_type = query_type
    query = ''.join(each for each in query if not each.isdigit())

    top150 = stopwords.words('english')[0:150]
    keywords_dict = {}
    query = query.split()
    # prepare the dictionary keys based on the query
    for each in query:
        each_lower = each.lower()
        each_lower = ps.stem(each_lower)
        if each_lower not in top150:
            keywords_dict[each_lower] = []
            # open the appropriate file depending on the word
            file = 'FINAL.txt'

            with open(files_dir + file) as fp:
                for line in fp:
                    term = re.findall(r'"(.*?)" :', line)
                    # if the term exists
                    if term is not None and len(term) is not 0:
                        term = term[0]
                        # if the keyword is equal to the dictionary term
                        if term in keywords_dict.keys():
                            if term == each_lower:
                                # get values and add to the keywords dict
                                try:
                                    values_list = line[line.index('\" :') + 3:]
                                    if values_list is not None and len(values_list) is not 0:
                                        values_list = ast.literal_eval(values_list)
                                        keywords_dict[term] = values_list
                                        # print(values_list)
                                        break
                                except:
                                    print('error:' + values_list)

    l_avg = 0
    # reading number of files
    num_docs = len(open('DOC_LENGTH_DICT.txt').readlines()) - 1
    print('num docs is', num_docs)
    # reading average document length
    try:
        l_avg = float(open('DOC_LENGTH_AVG.txt').readline())
        print('doc length average is ', l_avg)
    except ValueError:
        'error reading document length average'
    # the score for each of the results is calculated below. There are 3 cases
    # case 1: there is only 1 query term
    # case 2: there is more than 1 query term and it is an "and" query
    # case 3: there is more than 1 query term and it is an "or" query
    # for each of those cases, the apporpriate values are passed to the method calculate_doc_score
    if len(keywords_dict) == 1:
        print('\nResults for the single word query ' + "\"" + user_search + "\"")
        doc_ids = []
        for each in keywords_dict.values():
            doc_ids += make_list_from_dict_values(each)
        print("\nListed below are the results containing the keywords")
        calculate_doc_score(doc_id_list=doc_ids, dictionary=keywords_dict, k1=2, b=0.5, l_avg=l_avg,
                            num_docs=num_docs)

    elif query_type == 'and':
        print('\nResults for the query ' + "\"" + user_search + "\"")
        doc_ids = []
        for each in keywords_dict.values():
            doc_ids.append(make_list_from_dict_values(each))
        doc_ids = sorted(set.intersection(*map(set, doc_ids)))
        if len(doc_ids) is not 0:
            print("\nListed below are the results containing all of the keywords")
            calculate_doc_score(doc_id_list=doc_ids, dictionary=keywords_dict, k1=2, b=0.5, l_avg=l_avg,
                                num_docs=num_docs)
        else:
            print("No documents found\n")
    elif query_type == "or":
        doc_ids = []
        for each in keywords_dict.values():
            doc_ids.append(make_list_from_dict_values(each))
        doc_ids = sorted(set.union(*map(set, doc_ids)))
        if len(doc_ids) is not 0:
            print("\nListed below are the results containing some or all of the keywords")
            calculate_doc_score(doc_id_list=doc_ids, dictionary=keywords_dict, k1=10, b=1, l_avg=l_avg,
                                num_docs=num_docs)
        else:
            print("No documents found\n")


# method used to calculate the score of a list of documents
# it prints out the ranked results of the documents
# it prints out the score of the documents and the words that are contained in the document that match the word(s) in
# the query
# higher scored documents are listed higher than lower scored documents
# it takes a list of document ids, a frequency dictionary for all the query terms (taking into account compression)
# the constants k1 and b
# the document length average l_avg
# the total number of documents num_doc
def calculate_doc_score(doc_id_list, dictionary, k1, b, l_avg, num_docs):
    num_docs = num_docs
    l_avg = l_avg
    k1 = k1
    b = b
    score_dict = {}

    # for each document in the list of results, calculate their score
    for doc_id in doc_id_list:
        # for each word that is part of the query calculate their score and add it to the current document's score
        for word in dictionary.keys():
            doc_freq_of_term = len(dictionary[word])
            # we loop through each of the [doc_id, freq] in the list for a given term
            for word_and_freq in dictionary[word]:
                # if the 'tuple' we found  of format[doc_id, freq] matches the given doc_id, we grab the term frequency
                # we also get the document's id
                if word_and_freq[0] == doc_id:
                    term_freq_in_doc = word_and_freq[1]
                    # getting the doc length for given word
                    with open('DOC_LENGTH_DICT.txt') as fp:
                        try:
                            for index, line in enumerate(fp):
                                # read document and retrieve the document length value for given document id
                                # we know that doc_id is on line doc_id+1
                                if index == doc_id - 1 and index != "EOF":
                                    doc_len = line[line.index('\" :') + 3:]
                                    doc_len = doc_len.replace("\n", "")
                                    doc_len = doc_len.replace(",", "")
                                    doc_len = doc_len.replace(" ", "")
                                    doc_len = int(doc_len)
                                    # calculate score based on equation in book BM25
                                    # this is the score for the current word, for the current document
                                    # print ('*******TEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSTTTTTTTTTTT*')
                                    # print ('num docs', num_docs)
                                    # print ('doc freq of '+ word, doc_freq_of_term)
                                    # print ('term freq in doc', term_freq_in_doc)
                                    # print ('doc len', doc_len)
                                    # print ('l_avg', l_avg)
                                    # print ('*******TEEEEEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSSSSTTTTTTTTTTT*')
                                    score_bm25 = math.log10(num_docs / doc_freq_of_term) * (
                                            (k1 + 1) * term_freq_in_doc) / (
                                                         k1 * (1 - b) + b * (doc_len / l_avg) + term_freq_in_doc)

                                    # add to dictionary if doc_id is not there + add word(s) associated to that score
                                    # format of score_dict is
                                    # doc_id -> [score, [list of terms from the query also present in the doc]]
                                    if doc_id not in score_dict.keys():
                                        score_dict[doc_id] = [score_bm25, [word]]
                                    # if doc_id is in dictionary, add word if does not exist there
                                    # also increment the score for that document
                                    elif word not in score_dict[doc_id][1]:
                                        score_dict[doc_id][0] += score_bm25
                                        score_dict[doc_id][1].append(word)
                        except ValueError as e:
                            print('********************')
                            print(doc_id)
                            print(e)

    sorted_by_keywords = sorted(score_dict, key=lambda key: score_dict[key][1])
    list_display_order = (sorted(sorted_by_keywords, key=lambda key: score_dict[key][0], reverse=True))
    print('List of document ids')
    print(list_display_order)
    print('------------------------Found ' + str(len(list_display_order)) + ' documents------------------\n')
    doc_id_url_dict = get_urls_for_doc_id_list(list_display_order, 'https://www.concordia.ca/')

    # for each doc_id in the given list, return its score, its id, and the keywords that are both in the query and
    # the document
    for each_id in list_display_order:
        for doc_id in score_dict:
            if doc_id is each_id:
                print("document containing keyword(s): ", end="")
                print(score_dict[doc_id][1])
                line_values_score = '{:>3}  {:>12}'.format("document score:", score_dict[doc_id][0])
                line_doc_id = '{:>3}  {:>7}'.format("document id:", str(doc_id))
                # line_doc_url = '{:>3}  {:>7}'.format("document url:", doc_id_url_dict[doc_id])
                print(line_values_score)
                print(line_doc_id)
                print(doc_id_url_dict[doc_id])
                print('\n')
    print('*********************************************************************************')
    return score_dict


# this method is used to write to the final dictionary
# the final dictionary is a frequency dictionary
def read_files_and_write_final_dict_crawler(blocks_produced_from_tokenization, input_dir, output_dir):
    dict_filename_prefix = 'FINAL'
    my_dict = {}
    with contextlib.ExitStack() as stack:
        fp_list = [stack.enter_context(open(input_dir + fname)) for fname in blocks_produced_from_tokenization]
        done_reading = 0
        print(len(fp_list))
        keep_looping = True
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
                            my_dict = add_to_frequency_dict_with_array(term=term, doc_id_freq_array=values_list,
                                                                       my_dict=my_dict)
                    except Exception as e:
                        print(e)

                        print('content: ' + line_read)
                        print(line_read)
                        print(fp)
                        print(term)
                        print(line_read)
                        quit()

    print(len(my_dict))
    print_dict_to_file(output_dir=output_dir, filename=dict_filename_prefix, dict_name=my_dict, sorted_keys=True)


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


def tokenize_all_crawler(files, output_dir):
    top150 = stopwords.words('english')[0:150]
    block_dict = {}
    url_suffix_dict = {}
    # open each file, remove unneeded tags, tokenize
    newid = 1
    block_write = 0
    total_terms = 0
    ps = PorterStemmer()
    terms_dict = {}
    # todo create a dict containing key=docID, value=doc length
    doc_length_dict = {}
    doc_length_avg = 0
    newid = 0
    print('starting to write a dictionary every 500 files...')
    for file in files:
        with open(file) as fp:
            newid += 1
            # make sure to reset the doc_length to 0, before reading a new file
            print("file is", file)
            # keep track of the newid associated with the link to concordia.ca page
            url_suffix_dict[newid] = file[9:]
            doc_length = 0
            soup = BeautifulSoup(fp, 'html.parser')
            text = soup.get_text()
            text = ''.join(each for each in text if not each.isdigit())
            text = text.lower()
            text = nltk.word_tokenize(text)
            # if token is not in top 150
            text = [each for each in text if each not in top150]

            # use of porter stemmer for the table 5.1 but not for the final dictionary that was queried
            text = [ps.stem(each) for each in text]
            total_terms += len(text)

            # increment id per file

            # each word becomes a token in a dictionary. Every 500 terms, write those to disk
            for word in text:
                # increase doc length for every word read
                doc_length += 1
                # put all terms in a separate dictionary in order to delimitate the first word in the 25k words per
                # block
                block_dict = add_to_frequency_dict(term=word, doc_id=newid, my_dict=terms_dict)
                # this word signals the end of an article
            print('end of file')
            # at the end of the file, assign the length of the file to a newid in the doc_length_dict
            doc_length_dict[newid] = doc_length

            # when reaching the end of a document, increment the document's length, which will be divided at
            # the end to give the doc length average
            doc_length_avg += doc_length

            # when reaching the file 500, write all the content of the current dictionary (containing 500 files
            # terms and frequency)
            if newid % 500 is 1 and newid is not 1:
                if len(str(block_write)) is 1:
                    block_prefix = "BLOCK0"
                else:
                    block_prefix = "BLOCK"
                print('about to print to disk')
                print_dict_to_file(output_dir=output_dir, filename=block_prefix + str(block_write),
                                   dict_name=block_dict, sorted_keys=True)
                # increment block number
                block_write += 1
                # reset dictionary
                block_dict = {}
    # remaining that has not been written to disk is written to the last block
    if len(block_dict) is not 0:
        print('last block to write with remaining terms')
        print(block_write)
        if len(str(block_write)) is 1:
            block_prefix = "BLOCK0"
        else:
            block_prefix = "BLOCK"
        print('about to print to disk')
        # printing the frequency dictionary
        print_dict_to_file(output_dir=output_dir, filename=block_prefix + str(block_write), dict_name=block_dict,
                           sorted_keys=True)
    print('total number of terms ' + str(total_terms))
    terms_ordered = []
    for i in sorted(terms_dict.keys()):
        terms_ordered.append(i)

    # this gives back the 3 terms that start each of the blocks respectively
    print(len(terms_ordered))
    # try:
    #     print('first block value' + terms_ordered[0])
    #     print('first block value' + terms_ordered[25000])
    #     print('first block value' + terms_ordered[50000])
    # except:
    #     print('array out of bounds')
    # print('test')
    # disk_write = open("test.txt", "w+")
    # for each in terms_ordered:
    #     disk_write.write(each)
    #     disk_write.write('\n')
    # disk_write.close()

    doc_length_avg = doc_length_avg / len(doc_length_dict)
    print('doc length average ' + str(doc_length_avg))
    disk_write = open("DOC_LENGTH_AVG.txt", "w+")
    disk_write.write(str(doc_length_avg))
    disk_write.close()
    print_dict_to_file(output_dir='', filename='DOC_LENGTH_DICT', dict_name=doc_length_dict, sorted_keys=True)

    # printing the urls and associated id
    print_dict_to_file(output_dir='', filename='CONCORDIA_URLs', dict_name=url_suffix_dict,
                       sorted_keys=False)
