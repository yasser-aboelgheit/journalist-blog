from django.views.generic import TemplateView, DetailView
from about_me.models import AboutMePage
from prizes.models import Prize

class AboutMeView(TemplateView):
    template_name = 'about_me/about-me.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['pictures'] = AboutMePage.objects.first()
        data['prizes'] = Prize.objects.all()
        return data