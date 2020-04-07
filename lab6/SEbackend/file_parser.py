# simple wiki dump converted to plain text provided by:
# https://github.com/LGDoor/Dump-of-Simple-English-Wiki
import os
from Article import Article
from stopwords import stopwords
from nltk.stem import PorterStemmer
from typing import List

# chars forbidden in windows filenames (added () for clarity )
windows_forbidden = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|", "(", ")"]

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
                save = False
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

    # tokenizing
    content = "".join(file.readlines()).lower()
    for ch in ['.', ',', ':', '(', ')', '"', "'s"]:
        content = content.replace(ch, "")
    words = content.split()

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

    article = Article(title, stemmed_words, article_path)
    return article




