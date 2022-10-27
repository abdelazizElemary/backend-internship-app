from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

class BookList(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

