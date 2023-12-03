from django.db import models
from solo.models import SingletonModel


class AboutMePage(SingletonModel):
    wide_image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
