from rest_framework import serializers
from BookstoreData.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'