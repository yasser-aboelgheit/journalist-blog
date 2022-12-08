from django.shortcuts import render
from .models import Investigation
# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView, DetailView

class InvestigationListView(ListView):
    model = Investigation
    template_name = 'investigations/investigation_list.html'

class InvestigationDetialView(DetailView):
    model = Investigation
    template_name = 'investigations/investigation_detail.html'