from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(request.method, SAFE_METHODS)
        if request.method in SAFE_METHODS:
            return True
        print(request.user)
        print(obj.owner)
        return request.user == obj.owner
