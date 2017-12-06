#main file where everything will take place.
from WebParser import *
from NYTapi import *
from DataProcessor import *


categories = ["word","us","politics","ny","business","opinion","tech","science","health","sports","arts","style","food","Travel","magazine","t-magazine","realestate"] #the sections of the nytimes. to be used for clustering.


def main():
    articles = [] #will be holding a list of articles for nlp processing
    nyt = NewYorkTimes()
    urls = nyt.process_nyt()
    dp = DataProcessor()
    wp = WebParser()
    for url in urls:
        articles.append(wp.extract_body(url))
    # freq_words = dp.process(articles[0])
    # print(freq_words)
    words =[]
    print(articles) #shows the articles coming out.
    
    for article in articles:
        
        articlearr = article.split(" ")
        for term in articlearr:
            print(term)
            words.append(term)

    #doc_freq, term_frequency_document = dp.inverted_index(articles)


main()