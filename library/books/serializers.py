#import model
from .models import Book
#import serializer
from rest_framework import serializers

# Create your serializers here.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('Name', 'Author', 'publish_date', 'category')