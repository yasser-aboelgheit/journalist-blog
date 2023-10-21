from articles.models import Article, ArticleTypeChoices
# Create your views here.
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Article
    template_name = 'blogs/blogs_list.html'

    def get_queryset(self, **kwargs):
       qs = super().get_queryset(**kwargs)
       return qs.filter(type=ArticleTypeChoices.BLOG)

class BlogDetialView(DetailView):
    model = Article
    template_name = 'blogs/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.number_of_visits +=1
        blog.save()
        return super().dispatch(request, *args, **kwargs)
