from django.contrib import admin
from .models import MainSection, FirstSection, SecondSection, Tags
from solo.admin import SingletonModelAdmin

class MainSectionAdmin(SingletonModelAdmin):
    pass


class FirstSectionAdmin(SingletonModelAdmin):
    pass


class SecondSectionAdmin(SingletonModelAdmin):
    pass

admin.site.register(MainSection, MainSectionAdmin)
admin.site.register(FirstSection, FirstSectionAdmin)
admin.site.register(SecondSection, SecondSectionAdmin)


admin.site.register(Tags)