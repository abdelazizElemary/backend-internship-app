from blogs.models import Author, Blog
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id','username', 'password']

        extra_kwargs = {
            "password": {"write_only": True},
        }
    
    def create(self, validated_data):
        user = Author.objects.create(
        username=validated_data['username'],
        password = make_password(validated_data['password'])
        )
        return user
