from django.db.models import fields
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'publishDate',
                  'author', 'category', 'date_created', 'date_updated')
