class Search_struct:
    def __init__(self, articles):
        self.articles = articles
        self.dictionary = self.create_dictionary()

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
        # TODO add 2-way access? +['word0', 'word1', ..]
        return dictionary