from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    publish_data = models.DateTimeField(auto_now_add=True )
    category = models.CharField(max_length=150)