from django.urls import path
from .views import CoveragesListView, CoveragesDetialView

urlpatterns = [
    path('', CoveragesListView.as_view(), name='coverage_list'),
    path('coverage/<int:pk>/', CoveragesDetialView.as_view(), name='coverage_detail'),
]
