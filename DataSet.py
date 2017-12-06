#main file where everything will take place.
from WebParser import *
from NYTapi import *
from DataProcessor import *


categories = ["word","us","politics","ny","business","opinion","tech","science","health","sports","arts","style","food","Travel","magazine","t-magazine","realestate"] #the sections of the nytimes. to be used for clustering.

def generate_word_set(articles): #function that returns a set of words
    words = []
    for article in articles:
        article.replace("."," ")
        articlearr = article.split(" ")
        for term in articlearr:
            #print(term)
            words.append(term)
    
    bag_of_words = set(words) #unique set of words
    return bag_of_words



def main():
    articles = [] #will be holding a list of articles for nlp processing
    nyt = NewYorkTimes()
    dp = DataProcessor()
    wp = WebParser()
    
    query = input("Enter a search query -> ")
    urls = nyt.process_nyt(query)
    for url in urls:
        articles.append(wp.extract_body(url))
    # freq_words = dp.process(articles[0])
    # print(freq_words)
    print(articles) #shows the articles coming out.
    
    bag_of_words = generate_word_set(articles)
    print(bag_of_words)

    doc_freq, term_frequency_document = dp.inverted_index(articles)
    similarity, sorted_doc_list = dp.bm25(articles,doc_freq,term_frequency_document,query) 

    print("doc_freq: ",doc_freq)
    print("\n")
    print("term_freq_document: ",term_frequency_document)
    print("\n")
    print("similarity: ",similarity)
    print("\n")
    print("sorted_doc_list: ",sorted_doc_list)
    


main()