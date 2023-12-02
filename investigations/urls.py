from django.urls import path
from .views import InvestigationListView, InvestigationDetialView, InvestigationVideoListView

urlpatterns = [
    path('', InvestigationListView.as_view(), name='investigation_list'),
    path('video/', InvestigationVideoListView.as_view(), name='investigation_video_list'),
    path('investigation/<int:pk>/', InvestigationDetialView.as_view(), name='investigation_detail'),
]
