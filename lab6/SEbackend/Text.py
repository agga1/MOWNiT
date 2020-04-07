import numpy as np
from nltk import PorterStemmer
from stopwords import stopwords

class Text:
    def __init__(self, text: str):
        self.words = self.process_text(text)  # list of words
        self.BOW = None     # created when dictionary will be provided
        self.dictionary = None

    def convert_to_BOW(self, dictionary: dict):
        self.dictionary = dictionary
        self.BOW = np.array([0]*len(dictionary))
        for word in self.words:
            # if word in dictionary.keys():
            self.BOW[dictionary[word]] +=1
        self.words = None  # free memory

    @staticmethod
    def process_text(text):
        # tokenizing
        text = text.lower()
        for ch in ['.', ',', ':', '(', ')', '"', "'s"]:
            text = text.replace(ch, "")
        words = text.split()

        # removing stop words
        filered_words = []
        for w in words:
            if w not in stopwords:
                filered_words.append(w)

        # stemming
        ps = PorterStemmer()
        stemmed_words = []
        for w in filered_words:
            stemmed_words.append(ps.stem(w))

        return stemmed_words

    def __repr__(self):
        if self.BOW is None:
            print("Warning! no BOW found")
            return str(self.words)
        return str(self.BOW)

class Article(Text):
    """
    Text with some metadata
    """
    def __init__(self, title: str, text: str, link: str = None):
        super().__init__(text)
        self.title = title
        self.link = link  # absolute path to the full article in txt form


