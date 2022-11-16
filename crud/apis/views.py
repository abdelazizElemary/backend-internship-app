from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from blogs.models import Blog, Author
from .serializers import BlogSerializer, AuthorSerializer
from .permissions import IsAuthor

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (IsAuthor,)
    
    def create(self, request):
        author = request.user.pk
        request.data._mutable = True
        request.data['blog_author'] = author 
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    
