import nltk
nltk.download('punkt')
import unidecode

def tokenize_sgm(articles, soup_obj):
    list_of_tuples = []
    if articles is not None:
        for each in articles:
            # if there is an id

            if soup_obj.find(newid=each['newid']) is not None:
                # if there is a body
                if soup_obj.find(newid=each['newid']).find("body") is not None:
                    # assign it to the key newid
                    body = soup_obj.find(newid=each['newid']).find("body").contents[0]
                    body = str(body.encode('utf-8'))
                    body = body.strip().rstrip().lower().replace('\\n', ' ').replace('\r', '').split()


                    list_of_tuples.extend(make_tuples(body, each['newid']))

    return list_of_tuples


def make_tuples(body, newid):
    tuples_list = []
    for word in body:
        tuples_list.append(tuple((word, newid)))
    return tuples_list


def spimi_invert(token_stream, newid):
    file = open('block.txt', 'w+')
    dict_block = {}
    counter = 0

    while counter <= 500:
        for token in token_stream:
            if token not in dict_block.keys():
                dict_block[token] = newid
            else:
                dict_block[token].append(newid)
    for key, value in sorted(dict_block.items()):
        file.write(key + ': ')
        id_list_str = ''
        for each_id in value:
            id_list_str += each_id + ', '
        file.write(id_list_str)
        file.write('\n')

    return file.name, newid
