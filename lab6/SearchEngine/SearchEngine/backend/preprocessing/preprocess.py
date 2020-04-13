from time import perf_counter
from SearchEngine.backend.classes.SearchStruct import SearchStruct
from SearchEngine.backend.preprocessing.text_parser import parse_to_separate_files, articles_from_files, \
    articles_from_dbArticles
import os

from search.models import Article


def to_SearchStruct(art_dir, art_count=1000) -> SearchStruct:
    """
    Converts input data (1 txt file) to SearchStruct
    :param art_count: only first max_count articles will be processed
    """
    start = perf_counter()
    if Article.objects.count() < art_count:
        articles = articles_from_files(art_dir, art_count)
    else:
        articles = articles_from_dbArticles(art_count)
    print(f"{len(articles)} articles processed")
    end1 = perf_counter()
    SS = SearchStruct(articles)
    end2 = perf_counter()
    print("creating Articles, creating Struct\n times: ", end1-start, end2-end1)
    return SS


def init_search(art_count=1000) -> SearchStruct:
    curr_dir = os.getcwd()
    art_dir = os.path.join(curr_dir, "articles")
    if (Article.objects.count() < art_count) and (not os.path.exists(art_dir) or len(os.listdir(art_dir))< art_count):
        dump_dir = os.path.join(curr_dir, "data", "simple_wiki.txt")
        parse_to_separate_files(dump_dir, art_dir, art_count)
    SS = to_SearchStruct(art_dir, art_count)
    return SS

