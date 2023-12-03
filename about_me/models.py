from django.db import models
from solo.models import SingletonModel


class AboutMePage(SingletonModel):
    wide_image = models.ImageField(null=True, blank=True, upload_to="images/about")
    image_section_one = models.ImageField(null=True, blank=True, upload_to="images/about")
    image_section_two = models.ImageField(null=True, blank=True, upload_to="images/about")
    image_section_three = models.ImageField(null=True, blank=True, upload_to="images/about")
    image_section_four = models.ImageField(null=True, blank=True, upload_to="images/about")
    image_section_five = models.ImageField(null=True, blank=True, upload_to="images/about")

    bio = models.TextField(null=True, blank=True)
