from .models import Blog
# Create your views here.
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blogs_list.html'

class BlogDetialView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.number_of_visits +=1
        blog.save()
        return super().dispatch(request, *args, **kwargs)
