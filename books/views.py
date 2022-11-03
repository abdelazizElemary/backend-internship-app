import imp
from django.shortcuts import render
from .models import Book
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


# http://127.0.0.1:8000/books/rest/cbv/   => Postman
# http://127.0.0.1:8000/books/api-token-auth/ => Get_Token


class CBV_List(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )

class  CBV_pk(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExists:
            raise Http404
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def find_book(request):
    books = Book.objects.filter(
        author = request.data['author'],
        name = request.data['name'],
        publish_data = request.data['publish_data'],
        category = request.data['category'],
    )
    serializer = BookSerializer(books, many= True)
    return Response(serializer.data)


@api_view(['POST'])
def new_book(request):
    book = Book()
    book.author = request.data['author']
    book.name = request.data['name']
    book.publish_data = request.data['publish_data']
    book.category = request.data['category']
    book.save()
    return Response(status=status.HTTP_201_CREATED)