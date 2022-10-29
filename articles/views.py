from django.shortcuts import render
from .models import Article
# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

class ArticleDetialView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'