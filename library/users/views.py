from django.shortcuts import render

# Create your views here.

from knox.models import AuthToken
from rest_framework import generics, permissions
from rest_framework.response import Response

from users.serializers import LoginSerializer, UserSerializer, CreateUserSerializer


class SignUp(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        signup_response = {"user": UserSerializer(user, context=self.get_serializer_context()).data,
                           "token": AuthToken.objects.create(user)[1]}
        return Response(signup_response)


Signup_view = SignUp.as_view()


class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login_response = {"user": UserSerializer(user, context=self.get_serializer_context()).data,
                          "token": AuthToken.objects.create(user)[1]}
        return Response(login_response)


login_view = Login.as_view()


class UserProfile(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


user_profile_view = UserProfile.as_view()
