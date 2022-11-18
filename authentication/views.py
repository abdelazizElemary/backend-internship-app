from rest_framework import permissions
from django.contrib.auth import login

from django.contrib.auth.models import User
from .serializer import RegistrationSerializer
from rest_framework import generics

from django.contrib.auth import login
from .permissions import LoggedOut  
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginView(KnoxLoginView):
    permission_classes = [LoggedOut]

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        temp = super(LoginView, self).post(request, format=None)
        return Response({
            'token': temp.data['token'],
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
            }
        })

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegistrationSerializer

    
