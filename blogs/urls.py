from django.urls import path
from .views import BlogListView, BlogDetialView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetialView.as_view(), name='blog_detail'),
]
