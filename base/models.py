from abc import abstractmethod
from datetime import datetime
from uuid import UUID, uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _
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
