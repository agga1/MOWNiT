from time import perf_counter
from scipy import sparse
from scipy.sparse import csc_matrix, lil_matrix
from scipy.sparse.linalg import svds, eigs
import numpy as np
from numpy import linalg as LA

from typing import List
from classes.Article import Article
from classes.Text import Text


class SearchStruct:
    def __init__(self, articles: List[Article]):
        """
        - Creates dictionary of words based on Articles list
        - updates their representation as bag_of_words
        - creates matrix word X article
        """
        self.articles = articles
        st = perf_counter()
        self.dictionary = self.create_dictionary()
        st1 = perf_counter()
        self.matrix = self.texts_to_matrix()
        st2 = perf_counter()
        self.scale_by_IDF()
        self.normalize()
        st3 = perf_counter()
        print(f"creating dict:  {st1-st}"
              f"\ntxt_tomx {st2-st1}"
              f"\nscaling and norm: {st3-st2}")

    def create_dictionary(self):
        """
        creates dictionary of all words which appear in articles
        :return: dictionary {"word": idx, ...}
        """
        words_set = set()
        for article in self.articles:
            words_set = words_set.union(set(article.text.words))
        dictionary = {}
        idx = 0
        for word in words_set:
            dictionary[word] = idx
            idx += 1
        return dictionary

    def texts_to_matrix(self): # TODO BOW outside class?
        # with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        #     BOWs = list(executor.map(lambda art: art.to_BOW_with_clean(self.dictionary), self.articles))
        BOWs = []
        for article in self.articles:
            BOWs.append(article.text.convert_to_BOW(self.dictionary))
            article.text = None  # free memory for optimization
        return np.array(BOWs, dtype=float).transpose()

    def scale_by_IDF(self):
        N = self.matrix.shape[1]
        IDF = np.log2(N / np.count_nonzero(self.matrix, axis=1))  # / logN/nw, nw-nr of documents in which word exists
        for i in range(len(self.dictionary)):
            self.matrix[i] *= IDF[i]  # TODO numpy way?

    def normalize(self):
        self.matrix /= LA.norm(self.matrix, axis=0)

    def search(self, query_text: str, top_k: int, lra_k=None):
        query = Text(query_text)
        query.convert_to_BOW(self.dictionary)
        query.normalize_BOW()
        mx = self.matrix if lra_k is None else self.remove_noise(lra_k)
        products = np.zeros(mx.shape[1])
        for c in range(mx.shape[1]):
            products[c] = np.dot(mx[:, c], query.BOW)
        best_articles_at = np.argpartition(products, -top_k)[-top_k:]
        results = [(self.articles[idx], products[idx]) for idx in best_articles_at]
        results = sorted(results, key=lambda res: res[1], reverse=True)
        print(f"searched phrase : {query_text}")
        for res in results:
            print(f"{res[0]}\n correlation: {res[1]}")

    def remove_noise(self, k=10):
        mx = lil_matrix(self.matrix)
        print(mx.shape)
        u, s, vt = svds(mx, k=k, which='LM')
        s1 = np.diag(s)
        lrapp = u@s1@vt
        # print(lrapp[1])
        return lrapp


