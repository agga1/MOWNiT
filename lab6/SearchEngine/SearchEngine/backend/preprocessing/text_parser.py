# simple wiki dump converted to plain text provided by:
# https://github.com/LGDoor/Dump-of-Simple-English-Wiki
import os
import concurrent.futures
from SearchEngine.backend.classes.Article import Article
from typing import List

# chars forbidden in windows filenames (added () for clarity )
windows_forbidden = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|", "(", ")"]

def parse_to_separate_files(filename, out_dir, max_count=10000): #TODO add output folder
    """
    creates folder with each article in different file
    :param out_dir: directory to which dump articles (preferably "articles")
    :param filename: name of txt file comprised of articles formatted like :
    title in separate line, after which content, at the end of content blank line
    :param max_count: create only first max_count articles
    :return: name of generated folder with articles
    """
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


def articles_from_files(files_dir: str, max_count=1000) -> List[Article]:
    article_paths = [os.path.join(files_dir, file) for file in os.listdir(files_dir)]
    article_paths = article_paths[:max_count]
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        articles = list(executor.map(file_to_article, article_paths))
    # os.rmdir(files_dir) TODO rm articles?
    return articles


def file_to_article(article_path: str) -> Article:
    """
    creates Article object based on txt file:
    represented as list of words (later to be converted as BOW, when dictionary will be built)
    """
    from search.models import Article as dbArticle
    file = open(article_path, "r", encoding="utf8")
    title = file.readline()[:-1]  # no \n
    text = "\n".join(file.readlines())
    article = Article(title, text, article_path)
    if len(dbArticle.objects.filter(title=title))==0:
        dbArt = dbArticle(title=title, content=text)
        dbArt.save()
        article.id = dbArt.id
    article.id = dbArticle.objects.get(title=title).id
    print(f"id of article {article} is {article.id}")
    return article

def articles_from_dbArticles(art_count=1000) -> list:
    from search.models import Article as dbArticle
    articles = []
    cnt = 0
    for art in dbArticle.objects.all():
        print(art.title)
        articles.append(Article(title=art.title, text=art.content, id=art.id))
        cnt+=1
        if art_count <=cnt:
            break
    return articles






