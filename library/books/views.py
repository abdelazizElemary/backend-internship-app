from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, User
from rest_framework import viewsets
from .serializers import BookSerializer, UserSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('Name')
    serializer_class = BookSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
