from rest_framework.response import Response
from BookstoreData.models import Books
from .serializers import BooksSerializer,  UserSerializer, RegisterSerializer
from api import serializers
from rest_framework.views import APIView
from rest_framework import authentication, permissions, generics
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class BooksList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        items = Books.objects.all()
        serializer = BooksSerializer(items, many=True)
        return Response(serializer.data)


class UpdateList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    #get book by ID
    def get(self, request, pk, format=None):
        Books = self.get_object(pk)
        serializer = BooksSerializer(Books)
        return Response(serializer.data)

    # add book
    def post(self, requset, pk=None, format=None):
        serializer = BooksSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # delete book
    def delete(self, request, pk, format = None):
        try:
            book = Books.objects.get(pk=pk)
            book.delete()
            return Response("DELETED")
        except Books.DoesNotExist:
            return Response("ID NOT FOUND")

    #update book
    def put(self, requset, pk):
        try:
            book = Books.objects.get(id=pk)
            serializer = BooksSerializer(instance=book, data=requset.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Books.DoesNotExist:
            return Response("ID NOT FOUND")

# Register API
class RegisterAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })




class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)