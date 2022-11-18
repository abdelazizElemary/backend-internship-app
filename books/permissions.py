from rest_framework import permissions


class GuestAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):        
        return not request.user.is_authenticated or request.user.is_staff
