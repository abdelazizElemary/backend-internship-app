from django.db import models
from django.contrib.auth.models import AbstractUser

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Author(AbstractUser):
	def __str__(self):
		return self.email

class Book(TimeStampedModel):
    Authors = models.ManyToManyField(Author)
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)

    def __str__(self):
        return self.Name