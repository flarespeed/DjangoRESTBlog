from rest_framework import permissions

class AdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff:
            return True

        fullpermission = False

        try:
            fullpermission = obj.user == request.user
        except AttributeError:
            pass
        try:
            if request.user == obj.thread.user:
                if request.method in ['DELETE', 'POST']:
                    return True
        except AttributeError:
            if not fullpermission:
                fullpermission = obj == request.user
        return fullpermission
