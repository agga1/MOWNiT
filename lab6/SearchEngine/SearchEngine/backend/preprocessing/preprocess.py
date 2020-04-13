from time import perf_counter
from SearchEngine.backend.classes.SearchStruct import SearchStruct
from SearchEngine.backend.preprocessing.text_parser import parse_to_separate_files, files_to_articles
import os

def to_SearchStruct(art_dir, max_count=1000) -> SearchStruct:
    """
    Converts input data (1 txt file) to SearchStruct
    :param max_count: only first max_count articles will be processed
    """
    start = perf_counter()
    articles = files_to_articles(art_dir, max_count)
    print(f"{len(articles)} articles processed")
    end1 = perf_counter()
    SS = SearchStruct(articles)
    end2 = perf_counter()
    print("creating Articles, creating Struct\n times: ", end1-start, end2-end1)
    return SS


def init_search(art_count=1000) -> SearchStruct:
    curr_dir = os.getcwd()
    art_dir = os.path.join(curr_dir, "articles")
    if not os.path.exists(art_dir) or len(os.listdir(art_dir))<art_count:
        dump_dir = os.path.join(curr_dir, "data", "simple_wiki.txt")
        parse_to_separate_files(dump_dir, art_dir, art_count)
    SS = to_SearchStruct(art_dir, art_count)
    return SS

# SS = init_search(400)
# query = "april latin is my favorite sweet pea winter month of the year"
# SS.search(query, 5)
# SS.search(query, 5, 100)
# SS.search(query, 5, 50)

