from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from articles.models import ArticleTypeChoices, Article
from .models import Documentary
from django.views.generic import ListView, DetailView

# class DocumentaryListView(ListView):
#     model = Documentary
#     template_name = 'documentaries/documentary_list.html'

#     def get(self, request):
#         return redirect(reverse('documentary_detail', kwargs={'pk':Documentary.objects.first().pk}))

class DocumentaryDetialView(DetailView):
    model = Article
    template_name = 'documentaries/documentary_detail.html'


class DocumentaryListView(ListView):
    model = Article
    template_name = 'documentaries/documentary_list.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(type=ArticleTypeChoices.DOCUMENTRY)
