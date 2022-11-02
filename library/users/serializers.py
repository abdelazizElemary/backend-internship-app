from abc import ABC

from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class CreateUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    def validate(self, request):
        print(request['username'])
        password1 = request['password']
        password2 = request['confirm_password']
        if password1 and password2 == password1:
            return request

        raise serializers.ValidationError("password and confirm password are different")

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        extra = {'first_name': validated_data['first_name'], 'last_name': validated_data['last_name']}

        user = MyUser.objects.create_user(validated_data['username'], validated_data['email'],
                                          validated_data['password'], **extra)
        return user


class LoginSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, request):
        user = authenticate(**request)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Username or Password .")
