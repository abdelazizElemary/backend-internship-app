from django.db import models

# Create your models here.

    
    
class Books(models.Model):
    Author = models.CharField(max_length=200)
    Name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    publish_date = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    