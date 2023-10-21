from django.shortcuts import render
from articles.models import ArticleTypeChoices, Article
# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class InvestigationListView(ListView):
    model = Article
    template_name = 'investigations/investigation_list.html'

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(type=ArticleTypeChoices.INVESTIGATION)

class InvestigationDetialView(DetailView):
    model = Article
    template_name = 'investigations/investigation_detail.html'
