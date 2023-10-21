from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from home.models import Tags
from base.models import BaseModel

class ArticleTypeChoices(models.TextChoices):
    ARTICLE = 0, "مقالة"
    COVERAGE = 1, "تغطية"
    BLOG = 2, "تدوينة حرة"
    INVESTIGATION = 3, "تحقيق"
class Article(BaseModel):
    
    title = models.CharField(max_length=255)
    type = models.CharField('type of article', max_length=3,
                             choices=ArticleTypeChoices.choices, default=0
    )
    image = models.ImageField(null=True, blank=True, upload_to="images/articles")
    snippet = models.TextField(null=True, blank=True)
    content = RichTextUploadingField()

    @property
    def get_snippet(self):
        return self.snippet[:100]


    class Meta:
        ordering = ('published_at',)
