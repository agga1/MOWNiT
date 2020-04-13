from django.urls import path

from . import views

app_name = 'search' # add namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('results/<query>', views.results, name='results'),
    path('find/', views.find, name='find'),
    path('<int:article_id>/', views.detail, name='detail'),

]