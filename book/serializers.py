from rest_framework.serializers import ModelSerializer
from book.models import Book, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Book
        fields = "__all__"

