from rest_framework.serializers import ModelSerializer
from book.models import Book, Category


def BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


def CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
