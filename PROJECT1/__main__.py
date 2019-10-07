from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
from spimi import *
import threading

global_counter = 0
with open('reut2-001.sgm') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    articles = soup.find_all('reuters')
    tuples = []
    articles_counter = 0
    if articles is not None:
        while articles_counter <= 500:
            for article in articles:
                global_counter += global_counter
                articles_counter += articles_counter
                tuples.extend(tokenize_sgm(article, soup))
            spimi_invert(tuples, global_counter)
        articles_counter = 0
