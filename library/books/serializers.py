#import model
from .models import Book, User
#import serializer
from rest_framework import serializers

# Create your serializers here.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['Name', 'Author', 'category', 'created', 'modified']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')