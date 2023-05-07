from django.db import models
from datetime import datetime


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    created_at: datetime = models.DateTimeField(
        name="created_at",
        auto_now_add=True,
    )

    updated_at: datetime = models.DateTimeField(
        name="updated_at",
        auto_now=True,
    )

    def __str__(self):
        return self.name