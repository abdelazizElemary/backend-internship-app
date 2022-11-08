from django.db import models
from datetime import datetime
from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import timezone

# Create your models here.
class LeadModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500)
    owner = models.ForeignKey(User, related_name="leads", null=True, on_delete=CASCADE)

    def __str__(self):
        return self.name
    

class Books(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True )
    created_time = AutoCreatedField(_('created_time'))
    updated_time = AutoLastModifiedField(_('updated_time'))
   
    

