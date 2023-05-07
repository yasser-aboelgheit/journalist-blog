from django.db import models
from solo.models import SingletonModel


class MainSection(SingletonModel):
    profile_pic = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

class FirstSection(SingletonModel):
    first_section_pic = models.ImageField(null=True, blank=True)
    first_section_title = models.CharField(null=True, blank=True, max_length=255)
    first_section_subtitle_title = models.CharField(null=True, blank=True, max_length=255)
    first_section_first_paragraph = models.TextField(null=True, blank=True)
    first_section_second_paragraph = models.TextField(null=True, blank=True)

class SecondSection(SingletonModel):
    second_section_pic = models.ImageField(null=True, blank=True)
    second_section_title = models.CharField(null=True, blank=True, max_length=255)
    second_section_subtitle_title = models.CharField(null=True, blank=True, max_length=255)
    second_section_first_paragraph = models.TextField(null=True, blank=True)

class Tags(models.Model):
    tag = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.tag
