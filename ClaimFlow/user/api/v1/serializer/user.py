from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import EmailValidator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.conf import settings
User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=255)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'confirm_password'
        ]
    def validate(self, attrs):
        pass1 = attrs.get("password")
        pass2  = attrs.pop("confirm_password")
        if pass1 != pass2:
            raise ValidationError(
                "Password Mismatch"
            )
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,validators=[EmailValidator])
    password = serializers.CharField(max_length=255)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except TokenError:
            self.fail("bad_token")

class RefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh_token = attrs["refresh"]
        try:
            token = RefreshToken(refresh_token)
            data = {
                "access": str(token.access_token)
            }
            if settings.SIMPLE_JWT.get("ROTATE_REFRESH_TOKENS"):
                if settings.SIMPLE_JWT.get("BLACKLIST_AFTER_ROTATION"):
                    try:
                        token.blacklist()
                    except AttributeError:
                        pass

                new_refresh = RefreshToken.for_user(token.user)
                data["refresh"] = str(new_refresh)

            return data
        except TokenError:
            raise serializers.ValidationError("Invalid or blacklisted token")


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "email", "created_at", "updated_at"]
