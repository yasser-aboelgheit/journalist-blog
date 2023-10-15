from base.models import BaseModel
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Podcast(BaseModel):
    episode_number = models.IntegerField()
    title = models.CharField(max_length=255)
    snippet = models.TextField()
    video = models.FileField(null=True,blank=True)
    content = RichTextUploadingField()
    image = models.ImageField(null=True, blank=True, upload_to="images/blogs")


    def __str__(self):
        return self.title