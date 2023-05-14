from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from base.models import BaseModel

class Documentary(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/investigations")
    snippet = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()

    @property
    def get_snippet(self):
        return self.snippet[:100]

    class Meta:
        ordering = ('published_at',)

    def __str__(self):
        return self.title