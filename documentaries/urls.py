from django.urls import path
from .views import DocumentaryListView, DocumentaryDetialView

urlpatterns = [
    path('', DocumentaryListView.as_view(), name='documentary_list'),
    path('documentary/<int:pk>/', DocumentaryDetialView.as_view(), name='documentary_detail'),
]
