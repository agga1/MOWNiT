import numpy as np
from typing import List
from Text import Article


class SearchStruct:
    def __init__(self, articles: List[Article]):
        """
        - Creates dictionary of words based on Articles list
        - updates their representation as bag_of_words
        - creates matrix word X article
        """
        self.articles = articles
        self.dictionary = self.create_dictionary()
        self.update_articles_with_BOW()
        self.matrix = self.get_matrix()

    def create_dictionary(self):
        """
        creates dictionary of all words which appear in articles
        :return: dictionary {"word": idx, ...}
        """
        words_set = set()
        for article in self.articles:
            words_set = words_set.union(set(article.words))
        dictionary = {}
        idx = 0
        for word in words_set:
            dictionary[word] = idx
            idx += 1
        return dictionary

    def update_articles_with_BOW(self):
        for article in self.articles:
            article.convert_to_BOW(self.dictionary)

    def get_matrix(self):
        term_by_doc = np.array([a.BOW for a in self.articles], dtype=float).transpose()
        # IDF multiplication TODO log2?
        N = term_by_doc.shape[1]
        IDF = np.log2(N / np.count_nonzero(term_by_doc, axis=1))  # / nr of documents in which word exists
        for i in range(len(self.dictionary)):
            term_by_doc[i] *= IDF[i]  # TODO numpy way?
        return term_by_doc
