from rest_framework import viewsets
from rest_framework.response import  Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action,authentication_classes,permission_classes

from organization.models import Organization
from organization.api.v1.serializer.org_serializer import OrganizationSerializer


class OrganizationViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

