import nltk
import string

nltk.download('punkt')


def tokenize_sgm(article, soup_obj):
    tuples = []
    if soup_obj.find(newid=article['newid']) is not None:
        # if there is a body
        if soup_obj.find(newid=article['newid']).find("body") is not None:
            # assign it to the key newid
            body = soup_obj.find(newid=article['newid']).find("body").contents[0]
            # body = body.strip().rstrip().lower().replace('\\n', ' ').replace('\r', '')
            # body = body.translate(string.punctuation).split()
            body = nltk.word_tokenize(body)
            tuples.extend(make_tuples(body, article['newid']))
    return tuples


def tokenize_sgm_articles(articles, soup_obj):
    tuples = []
    for article in articles:
        if soup_obj.find(newid=article['newid']) is not None:
            # if there is a body
            if soup_obj.find(newid=article['newid']).find("body") is not None:
                # assign it to the key newid
                body = soup_obj.find(newid=article['newid']).find("body").contents[0]
                tokenized_body = nltk.word_tokenize(body)
                tuples.extend(make_tuples(tokenized_body, article['newid']))
    for each in tuples:
        print(each)
    return tuples


def make_tuples(body, newid):
    tuples_list = []
    for word in body:
        tuples_list.append(tuple((word, newid)))
    return tuples_list

# def spimi_invert(token_stream, counter):
#     # token_stream_to_dict = dict(token_stream)
#     file = open('block' + str(counter)+'.txt', 'a')
#     dict_block = {}
#
#     for term, article_id in token_stream_to_dict.items():
#         if term not in dict_block.keys():
#             dict_block[term] = article_id
#         else:
#             if article_id not in dict_block[term].values():
#                 dict_block[term].append(article_id)
#     for key, value in sorted(dict_block.items()):
#         file.write(key + ': ')
#         id_list_str = ''
#         for each_id in value:
#             id_list_str += each_id + ', '
#         file.write(id_list_str)
#         file.write('\n')
#     return file.name
