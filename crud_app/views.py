from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets

class BookAPI(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()