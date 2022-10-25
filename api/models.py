from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    publishDate = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
