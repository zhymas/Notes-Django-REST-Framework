from rest_framework.permissions import BasePermission

class IsAnAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):

        return obj.author == request.user if hasattr(obj, 'author') else False
