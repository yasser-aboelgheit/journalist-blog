from django.views.generic import TemplateView, CreateView
from articles.models import Article

class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['articles'] = Article.objects.all()
        return data
