from rest_framework import permissions
from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookPermission(permissions.BasePermission):
    # set permission list action for all , and remaining actions  must be authenticated
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'destroy':
            # get book id from url then check if the user have access to delete it or not
            try:
                book__id = int(request.path[7:-1])
            except ValueError:
                raise ValidationError("Not found")
            book = Book.objects.get(id=book__id)
            if book is None:
                raise ValidationError("Not found")
            return request.user.is_authenticated and request.user == book.author
        else:
            return request.user.is_authenticated
