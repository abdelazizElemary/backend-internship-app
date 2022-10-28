from rest_framework import viewsets
from rest_framework.response import Response
from book.models import Book, Category

from book.serializers import BookSerializer, CategorySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # we need to override create method to be able to add categories with their IDs
    def create(self, request, *args, **kwargs):
        categories = request.data.pop('categories', [])
        request.data['categories'] = []
        bookser = BookSerializer(data=request.data)
        bookser.is_valid(raise_exception=True)
        book = bookser.save()
        categories = Category.objects.filter(id__in=categories)
        book.categories.add(*categories)
        return Response(BookSerializer(book).data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
