from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from .models import Documentary
from django.views.generic import ListView, DetailView

class DocumentaryListView(ListView):
    model = Documentary
    template_name = 'investigations/documentary_list.html'

    def get(self, request):
        return redirect(reverse('documentary_detail', kwargs={'pk':Documentary.objects.first().pk}))

class DocumentaryDetialView(DetailView):
    model = Documentary
    template_name = 'investigations/documentary_detail.html'