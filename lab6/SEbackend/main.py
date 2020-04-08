from classes.Text import Text
from classes.SearchStruct import SearchStruct
from preprocessing.text_parser import parse_to_separate_files, files_to_articles
from time import perf_counter


def to_SearchStruct(art_dir, max_count=1000) -> SearchStruct:
    """
    Converts input data (1 txt file) to SearchStruct
    :param max_count: only first max_count articles will be processed
    """
    start = perf_counter()
    articles = files_to_articles(art_dir, max_count)
    print(f"{max_count} articles processed")
    end1 = perf_counter()
    SS = SearchStruct(articles)
    # a =articles[0].text.convert_to_BOW(SS.dictionary)
    # print(a)
    end2 = perf_counter()
    print("created dictionary, creating Struct\n times: ", end1-start, end2-end1)
    return SS


# wikipath = parse_to_separate_files("preprocessing/data/simple_wiki.txt", 4000)
SS = to_SearchStruct("articles", 110)
print("words in dict: ", len(SS.dictionary))
#
query = "april latin is my favorite sweet pea winter month of the year"
SS.search(query, 5)
SS.search(query, 5, 90)

