from django.urls import path
from about_me.views import AboutMeView

urlpatterns = [
    path('', AboutMeView.as_view(), name='about_me'),
]
