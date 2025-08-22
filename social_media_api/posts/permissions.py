from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    SAFE methods (GET/HEAD/OPTIONS): allowed for everyone
    Edit/Delete: only the owner (author) can modify
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        owner = getattr(obj, 'author', None)
        return owner == request.user
