from django.http import JsonResponse
from rest_framework import permissions
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from knox.views import LogoutView


class Register(APIView):
    serializer_class = RegisterSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        self.data = JSONParser().parse(request)
        self.serializer = RegisterSerializer(data=self.data)
        if self.serializer.is_valid():
            self.user = self.serializer.save()
            self.token = AuthToken.objects.create(self.user)
            return JsonResponse({
                "token": self.token[1],
                "user": UserSerializer(self.user).data
            }, status=201)
        return JsonResponse(self.serializer.errors, status=400)


class Login(APIView):
    serializer_class = LoginSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        self.data = JSONParser().parse(request)
        serializer = LoginSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return JsonResponse({
            "token": AuthToken.objects.create(user)[1],
            "user": UserSerializer(user).data
        }, status=200)


class Logout(LogoutView):
    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return JsonResponse({
            "detail": "logged out successfully"
        }, status=200)
