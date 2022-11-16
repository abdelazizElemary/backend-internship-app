from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True,write_only=True)

    def validate(self, request):
        password1 = request['password']
        password2 = request['confirm_password']
        if password1 and password2 == password1:
            return request

        raise serializers.ValidationError("Please sure that password and confirm password are identical .")

    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}

    def create(self, validated_data):
        extra_data = {'first_name': validated_data['first_name'], 'last_name': validated_data['last_name']}

        user = MyUser.objects.create_user(validated_data['username'], validated_data['email'],
                                          validated_data['password'], **extra_data)
        return user


class LoginSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, request):
        user = authenticate(**request)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Please enter the correct username and password for a staff account. Note "
                                          "that both fields may be case-sensitive..")


class ChangePasswordSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, request):
        password1 = request['new_password']
        password2 = request['confirm_new_password']
        if password1 and password2 == password1:
            return request

        raise serializers.ValidationError("Please sure that new password and  confirm password are identical . ")
