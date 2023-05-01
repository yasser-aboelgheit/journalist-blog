from django.views.generic import TemplateView, CreateView, ListView, DetailView
from articles.models import Article
from coverages. models import Coverage
from investigations.models import Investigation
from .models import Tags
# from flask import request


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.all()
        data['tags'] = Tags.objects.all()
        return data
class TagDetailView(DetailView):
    model = Tags
    template_name = 'tags/tag_detail.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.filter(tag=self.get_object())
        data['coverages'] = Coverage.objects.filter(tag=self.get_object())
        data['investigations'] = Investigation.objects.filter(tag=self.get_object())
        return data