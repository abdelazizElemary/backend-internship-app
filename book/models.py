from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    publish_date = models.DateField()
    categories = models.ManyToManyField(Category, related_name="books")

    def __str__(self):
        return self.name
