from bs4 import BeautifulSoup


def get_soup_obj(filename):
    with open(filename) as fp:
        return BeautifulSoup(fp, "html.parser")


def get_all_articles_in_file(soup_obj):
    return soup_obj.find_all('reuters')


# get all words to look for from word doc
def populate_inverted_index_dict_with_word_as_key(filename):
    inverted_index = {}
    with open(filename, "r") as fd:
        words_list = fd.read().splitlines()
        for word in words_list:
            word = word.rstrip()
            inverted_index[word] = []
    return inverted_index


def clean_up_text(string_input):
    # strip will remove all caps,
    return (string_input.rstrip().lower()).replace('\n', ' ').replace('\r', '').split()


def make_dict_with_newid_and_each_article_content(articles, soup_obj):
    newid_dict = {}
    for each in articles:
        if soup_obj.find(newid=each['newid']) is not None:
            # if there is a body
            if soup_obj.find(newid=each['newid']).find("body") is not None:
                # assign it to the newid
                newid_dict[each['newid']] = clean_up_text(soup_obj.find(newid=each['newid']).find("body").contents[0])
            # if there is no body and no place
            else:
                newid_dict[each['newid']] = ""
    return newid_dict


def populate_inverted_index_dict_with_newid_as_values(newid_dict, inverted_index):
    for newid in newid_dict:
        for word in inverted_index:
            if any(word in each_article_word for each_article_word in newid_dict[newid]):
                inverted_index[word].append(newid)
    return inverted_index


def print_inverted_index(inverted_index):
    for key in inverted_index:
        print("word is " + key + " and is contained in the following articles: ", end="")
        for each in inverted_index[key]:
            print(each, end=", ")
        print('\n')