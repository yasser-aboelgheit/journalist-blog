from django.views.generic import TemplateView, DetailView
from about_me.models import AboutMePage
from prizes.models import Prize

class AboutMeView(TemplateView):
    template_name = 'about_me/about-me.html'

    def get_context_data(self, **kwargs):
        # dates_list = []
        data = super().get_context_data(**kwargs)
        data['pictures'] = AboutMePage.objects.first()
        data['prizes'] = Prize.objects.all()
        # data['tags'] = Tags.objects.all()
        # data["documentary_id"] = Article.objects.filter(type=ArticleTypeChoices.INVESTIGATION_VIDEO).first().id
        # dates = list(Article.objects.all().values_list("published_at",flat=True))
        
        # for i in dates: dates_list.append(f"{calendar.month_name[i.month]} {i.year}")
        # # data["dates"] = dates_list
        # data["dates"] = dates_list
        return data