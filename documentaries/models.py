from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Tags

class Documentary(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/investigations")
    snippet = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()
    tag = models.ManyToManyField(Tags, blank=True)
    published_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    @property
    def get_snippet(self):
        return self.snippet[:100]

    class Meta:
        ordering = ('published_at',)
