from django.urls import path
from home.views import HomePageView, TagDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     path('tag/<int:pk>/', TagDetailView.as_view(), name='tag_detail'),

]