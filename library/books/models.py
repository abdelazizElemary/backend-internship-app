from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from model_utils.models import TimeStampedModel

class Book(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField('Category', blank=True)

    class Meta:
        ordering = ['author']
        unique_together = ('author', 'title',)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




