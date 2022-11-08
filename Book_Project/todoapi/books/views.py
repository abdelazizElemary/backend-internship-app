from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BooksSerializer
from .models import Books
# Create your views here.
class BooksList(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()