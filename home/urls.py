from django.urls import path
from home.views import HomePageView, TagDetailView, search_view, archive_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),
    path('search/', search_view, name='search_view'),
    path('archive/', archive_view, name='archive_view'),
]
