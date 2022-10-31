from django.db import models
from datetime import datetime
from model_utils.fields import (
    AutoCreatedField,
    AutoLastModifiedField,
)
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=300)
    category = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True )
    created_time = AutoCreatedField(_('created_time'))
    updated_time = AutoLastModifiedField(_('updated_time'))
   
    

