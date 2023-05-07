from .models import Podcast
from django.views.generic import ListView, DetailView

class PodcastListView(ListView):
    model = Podcast
    template_name = 'podcast/podcast_list.html'

class PodcastDetialView(DetailView):
    model = Podcast
    template_name = 'podcast/podcast_detail.html'