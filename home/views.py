from django.views.generic import TemplateView, DetailView
from articles.models import Article, ArticleTypeChoices
from .models import Tags
from documentaries.models import Documentary

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.filter(type=ArticleTypeChoices.ARTICLE)[:6]
        data['tags'] = Tags.objects.all()
        data["documentary_id"] = Documentary.objects.last().id
        return data
class TagDetailView(DetailView):
    model = Tags
    template_name = 'tags/tag_detail.html'
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.filter(tag=self.get_object())
        return data