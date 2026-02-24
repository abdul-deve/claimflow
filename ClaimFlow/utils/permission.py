from rest_framework.permissions import BasePermission
from user.models import UserRole,Roles


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        role = Roles.objects.get(name='admin')
        return UserRole.objects.get(user=user,role=role)


