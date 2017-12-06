#main file where everything will take place.
from WebParser import *
from NYTapi import *






def main():
    articles = [] #will be holding a list of articles for nlp processing
    # nyt = NewYorkTimes()
    # urls = nyt.process_nyt()
    wp = WebParser()
    articles.append(wp.extract_body())

    # Sprint(articles)
main()