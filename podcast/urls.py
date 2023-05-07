from django.urls import path
from .views import PodcastListView, PodcastDetialView

urlpatterns = [
    path('', PodcastListView.as_view(), name='podcast_list'),
    path('podcast/<int:pk>/', PodcastDetialView.as_view(), name='podcast_detail'),
]
