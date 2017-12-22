#main file where everything will take place.
from WebParser import *
from newsapi import *
from DataProcessor import *
from Clustering import *
import ast

def check_url(url): #to be used if getting articles for the first time
    url_snippets = url.split(".")
    for snippet in url_snippets:
        if snippet == 'foxnews':
            return snippet
        elif snippet == 'nytimes':
            return snippet
    return snippet

# #to be used if getting urls for the first time
# def getUrlsFromTxt(): #helper function to get the files from text
#     file = open('urls2.txt','r').read()
#     urls = file.split('\n')
#     return urls


def main():
    c = Clustering()#uses scikit library to get tf-idf of the terms k means clustering
    api = NewsApi() #used to return a list of urls from the api
    #urls = getUrlsFromTxt()#only if you don't have a text file
    dp = DataProcessor()#processing functions

    query = input("enter a search query -> ") #input a search query
    file = open('articlebodies.txt','r').read() #articles that have already been extracted
    articles = ast.literal_eval(file) #will be holding a list of articles for nlp processing. list representation
    full_articles = [article for article in articles if len(article) > 0]#remove articles with empty bodies

    # returns a key cluster value array based dictionary for documents and vocabulary
    # computes tf-idf and k-means clustering
    vocabCluster, docCluster, k = c.clusterize(full_articles)
    
    
    cluster_similarity = {}#rank clusters through the similarirt score
    sorted_doc_list_cluster = {} #holds the sorted_doc_list of each cluster
    for i in range(k):#iterate through k clusters
        doc_freq,term_freq_document = dp.inverted_index(docCluster[i]) #generate inverted index of the docs in cluster k 
        similarity,sorted_doc_list = dp.tf_idf(docCluster[i],doc_freq,term_freq_document,query)#compute tf idf and similarity scores between doc and query for documents in cluster k
        fscore = 0
        for key,score in similarity.items():
            fscore += score #compute the similarity scores of all the documents
        cluster_similarity[i] = fscore
        print(i, " ", sorted_doc_list)
        sorted_doc_list_cluster[i] = sorted_doc_list
    print("\nsorted clusters")
    sorted_cluster_list = sorted(cluster_similarity,key=cluster_similarity.get,reverse=True)

    #print(sorted_cluster_list)
    print(sorted_doc_list_cluster[sorted_cluster_list[0]])
    #use the cluster with highest similarity score
    doc_id = int(input("which document from the above ids would you like to open? ->"))

    #while True:#will keep running until user terminates program
    
    print(docCluster[sorted_cluster_list[0]][doc_id])#print article 
    df,tfd = dp.inverted_index(docCluster[sorted_cluster_list[0]])
    similarity,sorted_doc_list = dp.tf_idf(docCluster[sorted_cluster_list[0]],df,tfd,docCluster[sorted_cluster_list[0]][doc_id])
    print("top 5 similar docs in cluster %d " %sorted_cluster_list[0] ,sorted_doc_list[:5])
    print("similarity scores: ",similarity)


    # for doc_id in sorted_doc_list_cluster[sorted_cluster_list[0]]:
    #     print(docCluster[sorted_cluster_list[0]][doc_id])


main()