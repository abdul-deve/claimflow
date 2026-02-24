from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions


from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured

from user.api.v1.serializer import MeSerializer, ChangePassword

from rest_framework_simplejwt.authentication import JWTAuthentication

from user.helpers import _change_password





User = get_user_model()


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        if self.action == "me":
            return MeSerializer
        elif self.action == "change_password":
            return ChangePassword
        else:
            raise ImproperlyConfigured(
                                        "There is no serializer for this action"
                                       )
    @action(
        methods=["get", "put", "patch"],
        detail=False,
        url_path="me",
        authentication_classes=[JWTAuthentication],
        permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request):
        if request.method == "GET":
            serializer = MeSerializer(instance=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == "PUT":
            serializer = MeSerializer(
                instance=request.user,
                data=request.data,
                partial=False
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


        if request.method == "PATCH":
            serializer = MeSerializer(
                instance=request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=["post"],
        detail=False,
        url_path="change_password",
        authentication_classes=[JWTAuthentication],
        permission_classes=[permissions.IsAuthenticated]
    )
    def change_password(self, request):
        user = request.user
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        old_password = serializer.validated_data.get("old_password")
        new_password = serializer.validated_data.get("new_password")
        if not user.check_password(old_password):
            return Response({"message": "Old password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)
        _change_password(user, new_password)
        return Response(
            {"message": "Password changed successfully"},
            status=status.HTTP_200_OK
        )





