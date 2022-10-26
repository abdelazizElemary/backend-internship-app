
from unicodedata import category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers
from rest_framework import status

# all routes


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Add': '/add/book',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


# add book
@api_view(['POST'])
def add_book(request):
    item = BookSerializer(data=request.data)

    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


# get a specific book (by category) or get all books
@api_view(['GET'])
def view_books(request):

    # checking for the parameters from the URL
    if request.query_params:
        category = request.query_params.get("category", None)
        if category:
            items = Book.objects.filter(category=category)
    else:
        items = Book.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = BookSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# update a book
@api_view(['PUT'])
def update_book(request, pk):
    item = Book.objects.get(pk=pk)
    data = BookSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# delete a book
@api_view(['DELETE'])
def delete_book(request, pk):
    item = Book.objects.get(pk=pk)
    if item:
        item.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
