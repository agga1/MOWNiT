import numpy as np

from file_parser import parse_to_separate_files, files_to_articles

def create_dictionary(articles):
    """
    creates dictionary of all words which appear in articles
    :return: dictionary {"word": idx, ...}
    """
    words_set = set()
    for article in articles:
        words_set = words_set.union(set(article.words))
    dictionary = {}
    idx = 0
    for word in words_set:
        dictionary[word] = idx
        idx += 1
    # TODO add 2-way access? +['word0', 'word1', ..]
    return dictionary

def by_IDF(term_by_doc, dictionary):
    N = term_by_doc.shape[1]
    IDF = np.log2(N/np.count_nonzero(term_by_doc, axis=1))  # nr of documents in which word exists
    for i in range(len(dictionary)):
        term_by_doc[i] *=IDF[i] # TODO numpy way?
    return term_by_doc

def get_data_matrix(articles):
    return np.array([a.BOW for a in articles], dtype=float).transpose()

def article_preprocessing(filename, max_count=20000):
    """
    Creates dictionary of words based on @filename (which is a single txt file comprising of articles)
    and Article objects with their representation as bag_of_words
    :return: matrix term_by_doc, articles
    """
    wikipath = parse_to_separate_files(filename, max_count)
    articles = files_to_articles(wikipath)
    dictionary = create_dictionary(articles)
    for article in articles:
        article.convert_to_BOW(dictionary)
    mx = get_data_matrix(articles)
    mx2 = by_IDF(mx, dictionary)


article_preprocessing("simple_wiki.txt", 3)
