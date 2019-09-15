from bs4 import BeautifulSoup

__filename_words_list = "all-places-strings.lc.txt"
__filename = "reut2-0000.sgm"


# currently works with a single file
# read article

def get_soup_obj(filename):
    with open(filename) as fp:
        return BeautifulSoup(fp, "html.parser")


def get_all_articles_in_file(filename, soup_obj):
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
        print('newid is: ' + newid)
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


soup = get_soup_obj(__filename)
__contents = get_all_articles_in_file(__filename, soup)
__newid_dict = make_dict_with_newid_and_each_article_content(__contents, soup)
__inverted_index = populate_inverted_index_dict_with_word_as_key(__filename_words_list)
__inverted_index = populate_inverted_index_dict_with_newid_as_values(__newid_dict, __inverted_index)
print_inverted_index(__inverted_index)
