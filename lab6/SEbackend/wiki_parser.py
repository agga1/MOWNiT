# simple wiki dump converted to plain text provided by:
# https://github.com/LGDoor/Dump-of-Simple-English-Wiki
import os
# chars forbidden in windows filenames (added () for clarity )
windows_forbidden = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|", "(", ")"]
from typing import List

class Article:
    def __init__(self, title: str, words: List[str], link: str = None):
        self.title = title
        self.link = link  # absolute path to the full article in txt form
        self.words = words  # list of words
        self.BOW = None  # created when dictionary will be provided
        self.dictionary = None

    def convert_to_BOW(self, dictionary):
        # TODO generate BOW
        # self.dict..=dict..
        # set self.words = None
        pass

    def __repr__(self):
        return self.title

    def text_to_words(self, content):
        words = content.split()
        return words


def parse_to_separate_files(filename, max_count=10000):
    """
    creates folder with each article in different file
    :param filename: name of txt file comprised of articles formatted like :
    title in separate line, after which content, at the end of content blank line
    :param max_count: create only first max_count articles
    :return: name of generated folder with articles
    """
    out_dir = os.path.join(os.getcwd(), "articles")
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    wiki = open(filename, "r", encoding="utf8")

    count = 0
    title = None
    content = ""
    save = True
    for line in wiki:
        if title is None:   # title
            title = line
            if any(x in title for x in windows_forbidden):
                save = False             # omits any articles with characters forbidden in Windows file names
        elif line != "\n":  # content
            content += line
        else:               # end of content
            if save:
                article_path = os.path.join(out_dir, title[:-1] + ".txt")  # coz title with \n
                with open(article_path, "w", encoding="utf-8") as article_file:
                    article_file.write(title+content)
                count += 1
                if count >= max_count:
                    break
            save = True
            title = None
            content = ""
    return out_dir


def files_to_articles(files_dir: str) -> List[Article]:
    articles = []
    for article_file in os.listdir(files_dir):
        article_path = os.path.join(files_dir, article_file)
        articles.append(file_to_article(article_path))
    return articles


def file_to_article(article_path: str) -> Article:
    """
    creates Article object based on txt file:
    represented as list of words (later to be converted as BOW, when dictionary will be built)
    """
    file = open(article_path, "r", encoding="utf8")

    title = file.readline()[:-1]  # no \n
    content = "".join(file.readlines()).lower()
    for ch in ['.', ',', ':', '(', ')', '"']:
        content = content.replace(ch, "")
    words = content.split()
    # TODO remove stop words
    # TODO stemming
    article = Article(title, words, article_path)
    return article


def create_dictionray(articles):
    """
    creates dictionary of all words which appear in articles
    :return: dictionary {"word": idx, ...}
    """
    # TODO union of article.words for article in articles


wikipath = parse_to_separate_files("simple_wiki.txt", max_count=2)
files_to_articles(wikipath)