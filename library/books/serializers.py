from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('id', 'author')


    def create(self, validated_data):
        author = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            author = request.user
        validated_data['author'] = author
        book = Book.objects.create(**validated_data)  # saving post object
        return book

    @staticmethod
    def validate_access(book_author, request_user):
        print(book_author.id, request_user.id)
        if not request_user or request_user.id != book_author.id:
            raise serializers.ValidationError({'message': "you haven't access to this book "})

    def update(self, instance, validated_data):
        request_user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            request_user = request.user
        self.validate_access(instance.author, request_user)

        instance.title = validated_data.get('title', instance.title)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.category = validated_data.get('category', instance.category)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

    @staticmethod
    def validate_access2(book_author, request_user):
        print(book_author.id, request_user.id)
        if not request_user or request_user.id != book_author.id:
            raise serializers.ValidationError({'message': "you haven't access to this book "})


