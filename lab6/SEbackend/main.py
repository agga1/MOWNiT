from Text import Text
from SearchStruct import SearchStruct
from text_parser import parse_to_separate_files, files_to_articles


def to_SearchStruct(filename, max_count=20000) -> SearchStruct:
    """
    Converts input data (1 txt file) to SearchStruct
    :return: SearchStruct
    """
    wikipath = parse_to_separate_files(filename, max_count)
    articles = files_to_articles(wikipath)
    return SearchStruct(articles)

def search_query(query, SearchStruct):
    query = Text(query)
    query.convert_to_BOW(SearchStruct.dictionary)
    print(query)

SS = to_SearchStruct("simple_wiki.txt", 3)
print(SS.matrix)
query = "august was a very interesting month"
search_query(query, SS)
