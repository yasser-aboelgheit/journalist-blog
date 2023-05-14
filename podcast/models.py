from base.models import BaseModel
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Podcast(BaseModel):
    episode_number = models.IntegerField()
    title = models.CharField(max_length=255)
    snippet = models.TextField()
    youtube_link = models.URLField()
    video = models.FileField()
    content = RichTextUploadingField()

    def __str__(self):
        return self.title