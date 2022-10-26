from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    book_category = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.book_name

