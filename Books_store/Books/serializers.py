from dataclasses import field
from distutils.command.build_scripts import first_line_re
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
