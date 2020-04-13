import numpy as np
from nltk import PorterStemmer
from SearchEngine.backend.preprocessing.stopwords import stopwords
from numpy import linalg as LA
import string
from multiprocessing import Pool

class Text:
    def __init__(self, text: str):
        self.words = self.process_text(text)  # list of words
        self.BOW = None     # created when dictionary will be provided
        self.dictionary = None

    def convert_to_BOW(self, dictionary: dict):
        self.dictionary = dictionary
        self.BOW = np.array([0.]*len(dictionary))
        for word in self.words:
            if word in dictionary.keys():
                self.BOW[dictionary[word]] +=1.
        self.words = None  # free memory
        return self.BOW

    def normalize_BOW(self):
        if np.count_nonzero(self.BOW) > 0:
            self.BOW /= LA.norm(self.BOW)


    @staticmethod
    def process_text(text):
        # lower and replace punctuation
        text = text.lower()
        for punct in set(string.punctuation):
            text = text.replace(punct, "")

        # tokenizing
        words = text.split()

        # removing stop words
        stop_words = stopwords
        words = [w for w in words if w not in stop_words]

        # stemming
        ps = PorterStemmer()
        words = [ps.stem(w) for w in words]
        words = [word for word in words if len(word) > 2]

        return words

    def __repr__(self):
        if self.BOW is None:
            print("Warning! no BOW found")
            return str(self.words)
        return str(self.BOW)
