from rest_framework import permissions
from rest_framework import permissions
from knox.auth import TokenAuthentication


class BookPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True

        else:
            return request.user.is_authenticated
