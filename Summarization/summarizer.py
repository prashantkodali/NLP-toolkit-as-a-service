'''
This file details two classes:
WordVectors:  For handling pre-trained word embeddings. Has two methods :
                1. for reading a word vector files;
                2) generating sentences embeddings

Summarizer: For orchestrating the complete summarization process.
                Interacts with WordVectors to generate sentence vectors.
            Exposes methods for :
                1. Geting sentence vectors from WordVectors.
                2. Running the clustering algorithm
                3. extracting nearest sentences to the centroids of the clusters.
                4. Orchestrator method to call these methods.

Uses pymagnitude library for quick and memory efficient handling of large word embeddings file.
'''


from pymagnitude import *

from sklearn.cluster import KMeans
from scipy.spatial.distance import cosine

import numpy
import re


splitter = re.compile('[\s,\n]+')

class WordVectors:
    def __init__(self, path):
        self.vectors = Magnitude(path)
        self.vector_dim = self.vectors.dim

    def get_word(self, word):
        try:
            return self.vectors.query(word)
        except:
            return numpy.zeros(self.vector_dim)

    def get_sentence(self, sentence):

        sentence = splitter.split(sentence.strip())
        s = numpy.zeros(self.vector_dim)
        for word in sentence:
            s += self.get_word(word)
        return s


class Summarizer:

    def __init__(self, word_vector_file):
        self.vectors = WordVectors(word_vector_file)


    def get_sentence_vectors(self, sentences):
        sentence_vectors = []
        for sentence in sentences:
            sentence_vectors.append(self.vectors.get_sentence(sentence))
        return sentence_vectors

    def get_clusters(self, sentence_vectors, num_clusters):
        kmeans = KMeans(n_clusters=num_clusters, random_state=0, verbose = 0, init = 'random').fit(sentence_vectors)
        return kmeans.cluster_centers_

    def get_cluster_sent_ids(self, sentence_vectors, clusters):
        distances = []
        cluster_sent_ids = []
        for c, cluster in enumerate(clusters):
            distances.append([])
            for sentence_vector in sentence_vectors:
                distances[c].append(cosine(cluster,sentence_vector))

            mins = numpy.argsort(distances[c])[:len(clusters)]
            for minx in mins:
                if minx not in cluster_sent_ids:
                    cluster_sent_ids.append(minx)
                    break

        return cluster_sent_ids

    def summarize(self, document, num_sents):
        sentences = document.split('.')
        sentence_vectors = self.get_sentence_vectors(sentences)
        sentence_clusters = self.get_clusters(sentence_vectors, num_sents)
        sentence_ids = self.get_cluster_sent_ids(sentence_vectors, sentence_clusters)
        sentence_ids = sorted(sentence_ids)
        return [sentences[s] for s in sentence_ids]
