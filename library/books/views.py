from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# for list books and creat new books
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

# for retrieve, update or delete a book
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

