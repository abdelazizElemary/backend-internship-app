from rest_framework.response import Response
from rest_framework.decorators import api_view
from BookstoreData.models import Books
from .serializers import BooksSerializer
from api import serializers


@api_view(['GET'])
def getBooks(request):
    items = Books.objects.all()
    serializer = BooksSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBooks(requset):
    serializer = BooksSerializer(data=requset.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteBook(request, pk):
    try:
        book = Books.objects.get(id=pk)
        book.delete()
        return Response("DELETED")
    except Books.DoesNotExist:
        return Response("ID NOT FOUND")

@api_view(['POST'])
def updateBook(requset, pk):
    try:
        book = Books.objects.get(id=pk)
        serializer = BooksSerializer(instance=book, data=requset.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except Books.DoesNotExist:
        return Response("ID NOT FOUND")