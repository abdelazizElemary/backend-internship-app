from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from books.models import Book
from .permissions import BookPermission
from .serializers import BookSerializer


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BookPermission]

    def perform_destroy(self, instance):
        current_user = self.request.user

        if instance.author.id != current_user.id:
            raise ValidationError("Unauthorized user")
        instance.delete()
