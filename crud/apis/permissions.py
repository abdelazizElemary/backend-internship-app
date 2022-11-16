from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif view.action == 'create':
            return False
        else:
            return obj.blog_author == request.user
        
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_authenticated