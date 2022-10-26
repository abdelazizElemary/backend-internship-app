from rest_framework import viewsets
from blogs.models import Blog, Author

from .serializers import BlogSerializer, AuthorSerializer


# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
