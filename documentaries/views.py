from .models import Documentary
from django.views.generic import ListView, DetailView

class DocumentaryListView(ListView):
    model = Documentary
    template_name = 'investigations/documentary_list.html'

class DocumentaryDetialView(DetailView):
    model = Documentary
    template_name = 'investigations/documentary_detail.html'