from django.urls import path
from home.views import HomePageView, TagListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     path('tag/<int:pk>/', TagListView.as_view(), name='tag_detail'),

]