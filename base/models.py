from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from home.models import Tags
from publisher.models import Publisher


class BaseModel(models.Model):
    """
    Base Model containing all the common columns
    """

    class Meta:
        abstract: bool = True

    created_at: datetime = models.DateTimeField(
        name="created_at",
        auto_now_add=True,
    )

    updated_at: datetime = models.DateTimeField(
        name="updated_at",
        auto_now=True,
    )

    published_on = models.ForeignKey(Publisher,
                                     null=True,
                                     blank=True, on_delete=models.deletion.DO_NOTHING)
    tag = models.ManyToManyField(Tags, blank=True)
    published_at = models.DateField(null=True, blank=True)
    source_link = models.URLField(null=True, blank=True)
    number_of_visits = models.IntegerField(default=0)

    def __str__(self):
        return self.title if self.title else self.pk