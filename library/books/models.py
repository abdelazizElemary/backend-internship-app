from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
#didn't work don't know why
from django_extensions.db.models import TimeStampedModel
# Create your models here.
class User(AbstractUser):
    
    pass

class Book(TimeStampedModel):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    #publish_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.Name
    