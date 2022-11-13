from rest_framework import permissions
from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.path[7:-1])
        print(view.action)
        if view.action == 'list':
            return True
        elif view.action == 'destroy':
            try:
                book_author_id = int(request.path[7:-1])
            except ValueError:
                raise ValidationError("Not found")
            book = Book.objects.get(id=book_author_id)
            if book is None:
                raise ValidationError("Not found")
            return request.user.is_authenticated and request.user == book.author
        else:
            return request.user.is_authenticated
