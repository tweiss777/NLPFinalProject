#THIS USES SCIKIT LEARN LIBRARY
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

class Clustering:



    def tf_idf(self,doc_list):
        vectorizer = TfidfVectorizer(stop_words='english')
        x = vectorizer.fit_transform(doc_list)


