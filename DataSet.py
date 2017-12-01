#main file where everything will take place.
from WebParser import *
from NYTapi import *
from DataProcessor import *






def main():
    articles = [] #will be holding a list of articles for nlp processing
    # nyt = NewYorkTimes()
    # urls = nyt.process_nyt()
    dp = DataProcessor()
    wp = WebParser()
    articles.append(wp.extract_body())
    # freq_words = dp.process(articles[0])
    # print(freq_words)

    print(articles)
main()