from email.policy import default
from django.db import models
from django.utils import timezone
from  django.contrib.auth.models import User

from model_utils.models import TimeStampedModel


# Create your models here.
class Book(TimeStampedModel):
    title = models.CharField(max_length=40, unique = True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    publish_date = models.DateTimeField(default=timezone.now)
    class Meta:
         # "-" for descending order
         ordering = ['-publish_date']

    def __str__(self):
        return self.title

