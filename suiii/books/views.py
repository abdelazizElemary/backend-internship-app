from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book
from rest_framework import viewsets
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('Name')
    serializer_class = BookSerializer
    

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
