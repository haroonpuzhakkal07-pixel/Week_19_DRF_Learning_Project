from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Only owner can modify
        return obj.owner == request.user