#main file where everything will take place.
from WebParser import *
from newsapi import *
from DataProcessor import *

def check_url(url):
    url_snippets = url.split(".")
    for snippet in url_snippets:
        if snippet == 'foxnews':
            return snippet
        elif snippet == 'nytimes':
            return snippet
    return snippet

def getUrlsFromTxt(): #helper function to get the files from text
    file = open('urls2.txt','r').read()
    urls = file.split('\n')
    return urls


def main():
    query = input("enter a search query -> ") #input a search query 
    articles = [] #will be holding a list of articles for nlp processing
    api = NewsApi() #used to return a list of urls from the api
    urls = getUrlsFromTxt()
    dp = DataProcessor()
    wp = WebParser()
    urlcount = 1
    bodies = open('articlebodies.txt','w')
    for url in urls: #iterate through list of urls
        print(urlcount,')', url)
        #split the url into snippets
        site = check_url(url)
        print('site -> ',site)
        if site == 'foxnews':
            articles.append(wp.extract_body_foxnews(url))
        elif site == 'nytimes':
            articles.append(wp.extract_body_nyt(url))
        urlcount += 1

    # freq_words = dp.process(articles[0])
    # print(freq_words)
    words =[]
    print(articles) #shows the articles coming out.
    
    for article in articles:
        articlearr = article.split(" ")
        for term in articlearr:
            #print(term)
            words.append(term)

    doc_freq, term_frequency_document = dp.inverted_index(articles)
    similarity, sorted_doc_list = dp.tf_idf(articles,doc_freq,term_frequency_document,query)
    
    print('doc_freq: ', doc_freq)
    print('term_frequency_document: ',term_frequency_document)
    print('similarity: ',similarity)
    print('sorted_doc_list: ',sorted_doc_list)
    bodies.close()






main()