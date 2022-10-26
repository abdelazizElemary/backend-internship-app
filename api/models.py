from django.db import models
from uuid import uuid4


# TimeStampedMode -> to track the time an item has been added or updated in the db
class TimeStampedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(TimeStampedModel):
    name = models.CharField(max_length=255)
    publishDate = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
