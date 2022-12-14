from django.views.generic import TemplateView, CreateView, ListView, DetailView
from articles.models import Article
from .models import Tags
# from flask import request


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.all()
        return data
class TagDetailView(DetailView):
    model = Tags
    template_name = 'tags/tag_detail.html'
    # def mytag(request):
    #     mytag = request.POST['tag_pk']  
    #     print ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #     print(mytag)
    # mypatient = request.POST['patient_pk']
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
        # data['articles'] = Article.objects.all()
        # data['tag'] = 
        
        # return data
    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     # filter(tag__icontains=tag)
    #     print("=====================================================================")
    #     print (queryset)
    #     print("=====================================================================")
    #     return queryset