from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Tags


class Article(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/articles")
    snippet = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()
    tag = models.ManyToManyField(Tags, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # article_type = models.char

    @property
    def get_snippet(self):
        return self.snippet[:100]
