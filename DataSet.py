#main file where everything will take place.
from WebParser import *
from newsapi import *
from DataProcessor import *


def main():
    query = input("enter a search query -> ")
    articles = [] #will be holding a list of articles for nlp processing
    api = NewsApi()
    urls = api.google_news_extract(query)
    url_set = set(urls)
    dp = DataProcessor()
    wp = WebParser()

    for url in urls:
        print(url)
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

    doc_freq, term_frequency_document = dp.inverted_index(articles)
    similarity, sorted_doc_list = dp.bm25(articles,doc_freq,term_frequency_document,query)




main()