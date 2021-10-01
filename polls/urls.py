from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # default home page URL
    path('', views.index, name='index'),
    # ex: /create
    path('create/', views.create, name='create'),
    # ex: /detail?qid=5
    path('detail/', views.detail, name='detail'),
    # ex: /results?qid=5
    path('results/', views.results, name='results'),
    # ex: /vote?qid=5
    path('vote/', views.vote, name='vote'),
    # ex: /search?question=Django
    # path('search', views.search, name='search')
]

