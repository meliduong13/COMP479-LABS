from bs4 import BeautifulSoup
from spimi import *

with open('reut2-001.sgm') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    articles = soup.find_all('reuters')
    tokenized_text_tuples = tokenize_sgm(articles, soup)
    # spimi_invert(tokenized_text,)
    # fp.close()

