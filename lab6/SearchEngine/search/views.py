from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse

from SearchEngine.backend.preprocessing.preprocess import init_search
from SearchEngine.backend.preprocessing.text_parser import article_to_display
from search.models import Article

searchStruct = None
answers = None

def index(request):
    global searchStruct, answers
    searchStruct, answers = None, None
    return render(request, 'search/index.html', {})

def start(request):
    global searchStruct, answers
    answers = None
    if request.method == 'GET':
        N = int(request.GET['articles_nr'])
        searchStruct = init_search(N)
    elif searchStruct is None:
        searchStruct = init_search(1000)
    return render(request, 'search/start.html', {})

def detail(request, article_id):
    global searchStruct
    article_path = searchStruct.articles[article_id].link # TODO read file
    article = article_to_display(article_path)
    return render(request, 'search/detail.html', {'article': article})

def results(request, query):
    global answers
    return render(request, 'search/results.html', {'query': query, 'answers': answers})

def find(request):
    global searchStruct
    global answers
    query = request.GET['query']
    use_SVD = 1 if request.GET['svd_opt']=="yes" else 0
    art_nr = len(searchStruct.articles)
    lra_k = min(90, art_nr-1) if use_SVD else None
    top_k = min(int(request.GET['quantity']), art_nr)
    answers = searchStruct.search(query, top_k=top_k, lra_k=lra_k)
    print("len:", len(answers))
    return redirect('search:results', query=query)
