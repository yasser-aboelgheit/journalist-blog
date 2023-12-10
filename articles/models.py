from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from base.models import BaseModel

class ArticleTypeChoices(models.TextChoices):
    ARTICLE = 0, "مقالة"
    COVERAGE = 1, "تغطية"
    BLOG = 2, "تدوينة حرة"
    INVESTIGATION_WRITTEN = 3, "تحقيق مكتوب"
    DOCUMENTRY = 4, "وثائقي"
    INVESTIGATION_VIDEO = 5, "تحقيق فيديو"

class Article(BaseModel):
    
    title = models.CharField(max_length=255)
    type = models.CharField('type of article', max_length=3,
                             choices=ArticleTypeChoices.choices, default=0
    )
    image = models.ImageField(null=True, upload_to="images/articles")
    snippet = models.TextField(null=True,)
    content = RichTextUploadingField()
    show_on_home_page = models.BooleanField(default=False)


    @property
    def get_snippet(self):
        return self.snippet[:100]


    class Meta:
        ordering = ('published_at',)
