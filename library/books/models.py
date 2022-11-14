
from django.db import models

from core.models import TimeStampedModel

from users.models import MyUser


# Create your models here.
class Book(TimeStampedModel):
    author = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=60, default='New Book')
    summary = models.TextField(blank=True)
    category = models.CharField(max_length=70, default='general')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
