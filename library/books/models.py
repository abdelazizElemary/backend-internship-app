from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from model_utils.models import TimeStampedModel

options = (
    ('Adventure stories', 'Adventure stories'),
    ('Classics', 'Classics'),
    ('Fantasy', 'Fantasy'),
    ('Historical fiction', 'Historical fiction'),
    ('Horror', 'Horror'),
    ('Humour and satire', 'Humour and satire'),
)

class Book(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=options, blank=True, null=True)

    class Meta:
        ordering = ['author']
        unique_together = ('author', 'book_name',)

    def __str__(self):
        return self.book_name



