from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Tags
from base.models import BaseModel


class Investigation(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to="images/investigations")
    snippet = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()
    tag = models.ManyToManyField(Tags, blank=True)
    published_at = models.DateField(null=True, blank=True)

    @property
    def get_snippet(self):
        return self.snippet[:100]

    class Meta:
        ordering = ('published_at',)
