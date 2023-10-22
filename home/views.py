from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from articles.models import Article, ArticleTypeChoices
from .models import Tags
from documentaries.models import Documentary
import calendar
from translate import Translator
from datetime import datetime


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        translator = Translator(to_lang="Arabic")
        dates_list = []
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.filter(type=ArticleTypeChoices.ARTICLE)[:6]
        data['tags'] = Tags.objects.all()
        data["documentary_id"] = Documentary.objects.last().id
        dates = list(Article.objects.all().values_list("published_at",flat=True))
        
        for i in dates: dates_list.append(f"{calendar.month_name[i.month]} {i.year}")
        # data["dates"] = dates_list
        data["dates"] = dates_list
        print(dates_list)
        return data
class TagDetailView(DetailView):
    model = Tags
    template_name = 'tags/tag_detail.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.filter(tag=self.get_object())
        return data

def search_view(request, *args, **kwargs):
    if request.method == 'POST':
        articles = Article.objects.filter(content__contains=request.POST["search"])

    return render(request, 'search/search.html', {'title': 'نتايج البحث', 'articles': articles})

def archive_view(request, *args, **kwargs):

    date_string = request.POST["archive-dropdown"]
    date_format = "%B %Y"  

    date = datetime.strptime(date_string, date_format)
    articles = Article.objects.filter(published_at__year=date.year, published_at__month=date.month)
    return render(request, 'search/search.html', {'title': request.POST["archive-dropdown"], 'articles': articles})
