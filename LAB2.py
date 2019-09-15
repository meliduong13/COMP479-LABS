from bs4 import BeautifulSoup

contents = ""
newid_dict = {}
inverted_index = {}
filename = "all-places-strings.lc.txt"

# currently works with a single file
# read article
with open("reut2-0000.sgm") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# get all words to look for from word doc
with open(filename, "r") as fd:
    words_list = fd.read().splitlines()
    for word in words_list:
        word = word.rstrip()
        inverted_index[word] = []
    print(inverted_index)


def clean_up_text(string_input):
    # strip will remove all caps,
    return (string_input.rstrip().lower()).replace('\n', ' ').replace('\r', '').split()


articles = soup.find_all('reuters')

for each in articles:
    if soup.find(newid=each['newid']) is not None:
        # if there is a body
        if soup.find(newid=each['newid']).find("body") is not None:
            # assign it to the newid
            newid_dict[each['newid']] = clean_up_text(soup.find(newid=each['newid']).find("body").contents[0])
        # if there is no body and no place
        else:
            newid_dict[each['newid']] = ""

for newid in newid_dict:
    print('newid is: ' + newid)
    for word in inverted_index:
        if any(word in each_article_word for each_article_word in newid_dict[newid]):
            inverted_index[word].append(newid)
        # if any('romania' in each_article_word for each_article_word in newid_dict[newid]):
        #     print('found romania')

# prints the dictionary that associates the words in the all-places-strings.lc.txt to the newid which contain the given words
for key in inverted_index:
    print("word is " + key + " and is contained in the following articles: ", end="")
    for each in inverted_index[key]:
        print(each, end=", ")
    print('\n')

# print('****')
# print(newid_dict['925'])
