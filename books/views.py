# from urllib import response
# from django.shortcuts import render
# from django.http import HttpResponse
# from rest_framework.response import Response


# def create(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
# # Create your views here.

# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from books.models import Book

# # class ListUsers(APIView):
# #     """
# #     View to list all users in the system.

# #     * Requires token authentication.
# #     * Only admin users are able to access this view.
# #     """

# #     def get(self, request, format=None):
# #         """
# #         Return a list of all users.
# #         """
# #         books = [book.title for book in Book.objects.all()]
# #         booksauthor = [book.author for book in Book.objects.all()]
# #         print(booksauthor)
# #         return Response(books)


# #     def post(self, request, format=None):
# #         """
# #         Return a list of all users.
# #         """
# #         books = [book.title for book in Book.objects.all()]
# #         return Response(books)

# from .models import Book
# from .serializers import BookSerializer
# from rest_framework import generics

# class BookList(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer   
    



# class BookViewSet(viewsets.ViewSet):
#     def list(self, request):
#         pass

#     def create(self, request):
#         pass

#     def retrieve(self, request, pk=None):
#         pass

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
