from turtle import title
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=60, blank=False)
    category = models.CharField(max_length=100, blank=True)
    publish_date = models.DateField(blank=True)

    def __str__(self) -> str:
        return self.title
