from rest_framework import permissions

class LoggedOut(permissions.BasePermission):
    def has_permission(self, request, view):        
        return not request.user.is_authenticated