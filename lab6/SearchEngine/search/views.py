from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from SearchEngine.backend.preprocessing.preprocess import init_search
from search.models import Article

searchStruct = None
answers = None

def index(request):
    global searchStruct, answers
    searchStruct = None
    answers = None
    return render(request, 'search/index.html', {})

def start(request):
    global searchStruct
    if request.method == 'GET':
        N = int(request.GET['articles_nr'])
        searchStruct = init_search(N)
    if searchStruct is None:
        searchStruct = init_search(1000) # deafult structure with 1000 articles
    return render(request, 'search/start.html', {})

def detail(request, article_id):
    global searchStruct
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'search/detail.html', {'article': article})

def results(request, query):
    global answers
    return render(request, 'search/results.html', {'query': query, 'answers': answers})

def find(request):
    global searchStruct
    global answers
    query = request.GET['query']
    use_SVD = 1 if request.GET['svd_opt']=="yes" else 0
    lra_k = min(90, len(searchStruct.articles)) if use_SVD else None
    top_k = min(int(request.GET['quantity']), len(searchStruct.articles))
    answers = searchStruct.search(query, top_k=top_k, lra_k=lra_k)
    print("len:",len(answers))
    return redirect('search:results', query=query)
