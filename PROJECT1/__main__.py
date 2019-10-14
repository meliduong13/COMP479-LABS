from multiprocessing.dummy import Pool as ThreadPool
from bs4 import BeautifulSoup
from spimi import *
import threading
import queue
from os import listdir
from os.path import isfile, join

bloc_counter = 0
files = [f for f in listdir('./files') if isfile(join('./files', f))]

tokenize(files)
# for file in files:
    # with open('./files/' + file) as fp:
    #     soup = BeautifulSoup(fp, "html.parser")
    #     articles = soup.find_all('reuters')
    #     tuples = []
    #     que = queue.Queue()
    #     threads_list = list()
    #     articles_counter = 0
    #
    #     if articles is not None:
    #         tuples.append(tokenize_sgm_articles(articles, soup))
