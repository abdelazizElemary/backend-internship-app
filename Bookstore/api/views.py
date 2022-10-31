from rest_framework.response import Response
from BookstoreData.models import Books
from .serializers import BooksSerializer
from api import serializers
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404


class BooksList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        items = Books.objects.all()
        serializer = BooksSerializer(items, many=True)
        return Response(serializer.data)


class UpdateList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Books = self.get_object(pk)
        serializer = BooksSerializer(Books)
        return Response(serializer.data)

    def post(self, requset, pk=None, format=None):
        serializer = BooksSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format = None):
        try:
            book = Books.objects.get(id=pk)
            book.delete()
            return Response("DELETED")
        except Books.DoesNotExist:
            return Response("ID NOT FOUND")

    def put(self, requset, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BooksSerializer(instance=book, data=requset.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Books.DoesNotExist:
            return Response("ID NOT FOUND")


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })