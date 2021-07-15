from rest_framework import permissions

class AdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        try:
            if request.user == obj.thread.user:
                return True
        except AttributeError:
            pass
        try:
            return obj.user == request.user
        except AttributeError:
            return obj == request.user