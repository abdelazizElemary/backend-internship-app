from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class MyUser(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    email = models.CharField(max_length=70, blank=True, null=True, unique=True)
    phone_no = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return "{}".format(self.email)
