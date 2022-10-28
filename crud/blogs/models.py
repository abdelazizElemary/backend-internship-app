from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Author(AbstractUser):

    def __str__(self):
        return self.username


class Blog(models.Model):
    blog_author = models.ForeignKey(Author,  on_delete = models.CASCADE)
    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.blog_title
