from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        label='Password', required=True)
    password2 = serializers.CharField(
        label='Password confirmation', required=True)

    def validate_password1(self, password1):
        validate_password(password1)
        return password1
    def validate(self, data):
        if data.get('password1') != data.get('password2'):
            print(data)
            raise serializers.ValidationError(
                {'password2': ["Passwords don't match"]})
        return data

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'], password=validated_data['password1'], email=validated_data['email'])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label='Username', required=True)
    password = serializers.CharField(label='Password', required=True)

    def validate(self, data):
        self.user = authenticate(**data)
        if self.user and self.user.is_active:
            return self.user
        raise serializers.ValidationError('Incorrect Credentials Passed.')
