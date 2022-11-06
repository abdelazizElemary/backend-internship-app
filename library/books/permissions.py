from rest_framework import permissions
from rest_framework import permissions


class BookPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action in ['create', 'retrieve', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        else:
            return False
