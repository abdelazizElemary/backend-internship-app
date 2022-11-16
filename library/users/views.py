from django.shortcuts import render

# Create your views here.

from knox.models import AuthToken
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import LoginSerializer, UserSerializer, ChangePasswordSerializer


class SignUp(generics.GenericAPIView):
    serializer_class = UserSerializer

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


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        current_user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not current_user.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Please enter the correct  password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            current_user.set_password(serializer.data.get("new_password"))
            current_user.save()
            change_password_response = {
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(change_password_response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


user_change_password_view = ChangePasswordView.as_view()
