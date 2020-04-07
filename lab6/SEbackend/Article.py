from typing import List
import numpy as np
class Text:
    def __init__(self, words: List[str]):
        self.words = words  # list of words
        self.BOW = None     # created when dictionary will be provided
        self.dictionary = None

    def convert_to_BOW(self, dictionary):
        self.dictionary = dictionary
        self.BOW = np.array([0]*len(dictionary))
        for word in self.words:
            self.BOW[dictionary[word]] +=1
        self.words = None  # free memory

    def __repr__(self):
        if self.BOW is None:
            print("Warning! no BOW found")
            return str(self.words)
        return str(self.BOW)

class Article(Text):
    """
    Text with some metadata
    """
    def __init__(self, title: str, words: List[str], link: str = None):
        super().__init__(words)
        self.title = title
        self.link = link  # absolute path to the full article in txt form


