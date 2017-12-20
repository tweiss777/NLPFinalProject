#THIS USES SCIKIT LEARN LIBRARY
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

class Clustering:



    def clusterize(self,doc_list):
        k = int(input("enter number of clusters")) #input by the user of the number of clusters
        vectorizer = TfidfVectorizer(stop_words='english')
        cluster_doc = {i: [] for i in range(k)} #key is the cluster number. value is an array of articles that are predicted to go to the cluster
        vocab_cluster = {i: [] for i in range(k)}
        x = vectorizer.fit_transform(doc_list)
        xa = x.toarray()
        
        model = KMeans(n_clusters=k,init='k-means++', max_iter=100, n_init=1)#initialize object
        model.fit(x) #performs k mean clustering

        centroids = model.cluster_centers_.argsort()[:,::-1]
        vocab = vectorizer.get_feature_names() # gets the name of the terms from the integers
        for i in range(k):
            for ind in centroids[i,0:]:
                vocab_cluster[i].append(vocab[ind])

        for doc in doc_list:
            y = vectorizer.transform([doc])
            prediction = model.predict(y)
            cluster_doc[prediction[0]].append(doc)

        return vocab_cluster, cluster_doc


