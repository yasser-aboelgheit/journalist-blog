from django.shortcuts import render
from .models import Article, ArticleTypeChoices
# Create your views here.
from django.views.generic import ListView, DetailView

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(type=ArticleTypeChoices.ARTICLE)


class ArticleDetialView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

    def dispatch(self, request, *args, **kwargs):
        article = self.get_object()
        article.number_of_visits +=1
        article.save()
        return super().dispatch(request, *args, **kwargs)
