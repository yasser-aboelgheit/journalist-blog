from django.urls import path
from .views import ArticleListView, ArticleDetialView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetialView.as_view(), name='article_detail'),
]
