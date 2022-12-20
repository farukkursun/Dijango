from rest_framework import permissions
# from rest_framework.permissions import BasePermission


class CustomIsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request,view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_stafy
