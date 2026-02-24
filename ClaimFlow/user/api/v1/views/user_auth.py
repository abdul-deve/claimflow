from rest_framework import viewsets
from django.contrib.auth import get_user_model
from user.api.v1.serializer import (UserRegisterSerializer,
                                              LoginSerializer,
                                              LogoutSerializer,
                                              RefreshSerializer,
                                              MeSerializer)
from django.contrib.auth import authenticate,logout
from rest_framework.decorators import  action
from rest_framework import status
from rest_framework.response import  Response
from rest_framework.exceptions import AuthenticationFailed
from user.helpers import get_tokens_for_user
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
User = get_user_model()


class AuthViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []


    def get_serializer_class(self):
        if self.action == "register":
            return UserRegisterSerializer
        elif self.action == "login":
            return LoginSerializer
        elif self.action == "logout":
            return LogoutSerializer
        elif self.action == "refresh":
            return RefreshSerializer
        return None

    @action(
        detail=False,
        url_name="register",
        url_path="register",
        methods=["post"]
    )
    def register(self,request):
        serializer_class = self.get_serializer_class()
        serializer=serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            data = {
                "message" : "User is Successfully Registered ",
                "tokens" : tokens
            }
            return Response(data,status.HTTP_201_CREATED)
        return serializer.errors

    @action(
        methods=['post'],
        detail=False,
        url_path="login",
        url_name='login',
    )
    def login(self,request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get("email")
            password = serializer.validated_data.get("password")
            if user := authenticate(request,username=email,password=password):
                data = {
                    "message" : "Login successfully ",
                    "tokens" : get_tokens_for_user(user),
                    "user" : MeSerializer(user).data
                }
                return Response(
                    data,
                    status.HTTP_200_OK
                )
            raise AuthenticationFailed(
                "Invalid Credentials"
            )
        return serializer.errors

    @action(
        methods=['post'],
        detail=False,
        url_path="logout",
        url_name="logout",
        authentication_classes=[JWTAuthentication],
        permission_classes=[permissions.IsAuthenticated]
    )
    def logout(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Logout successful"},
            status=status.HTTP_205_RESET_CONTENT
        )

    @action(
        methods=['post'],
        detail=False,
        url_path="refresh",
        url_name="refresh"
    )
    def refresh(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "message": "Token refreshed successfully",
                "tokens": serializer.validated_data
            },
            status=status.HTTP_200_OK
        )
    



