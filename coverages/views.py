from django.shortcuts import render
from .models import Coverage
# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class CoveragesListView(ListView):
    model = Coverage
    template_name = 'coverages/coverage_list.html'

class CoveragesDetialView(DetailView):
    model = Coverage
    template_name = 'coverages/coverage_detail.html'