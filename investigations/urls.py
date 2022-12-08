from django.urls import path
from .views import InvestigationListView, InvestigationDetialView

urlpatterns = [
    path('', InvestigationListView.as_view(), name='investigation_list'),
    path('investigation/<int:pk>/', InvestigationDetialView.as_view(), name='investigation_detail'),
]
