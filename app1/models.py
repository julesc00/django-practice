import uuid

from django.db import models
from django.urls import reverse


class University(models.Model):
    """Practicing best practices for models."""
    full_name = models.CharField(max_length=100, db_index=True)
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,

    )

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("university-detail", args=[str(self.id)])
