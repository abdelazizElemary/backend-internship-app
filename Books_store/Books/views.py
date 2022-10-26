from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book

# Crud Operations


# Read
class ListBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# update, Delete a book
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# create a new book
class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#  Delete a book
class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
