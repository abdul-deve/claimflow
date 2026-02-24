from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import OutstandingToken,BlacklistedToken
from django.contrib.auth import get_user_model
from django.db import transaction, IntegrityError
from django.db.models import Q
from user.models import UserRole,Roles
User = get_user_model()

def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


def logout_from_all_devices(user_id=None, email=None):
    if not user_id and not email:
        raise ValueError("Either user_id or email is required")

    try:
        if user_id:
            user = User.objects.get(id=user_id)
        else:
            user = User.objects.get(Q(email=email) | Q(username=email))
    except User.DoesNotExist:
        raise User.DoesNotExist("User not found")

    tokens = OutstandingToken.objects.filter(user=user)
    if not tokens.exists():
        return 0

    with transaction.atomic():
        BlacklistedToken.objects.bulk_create(
            [BlacklistedToken(token=token) for token in tokens],
            ignore_conflicts=True,
        )

    return tokens.count()

def _change_password(user, new_password):
    with transaction.atomic():
        user.set_password(new_password)
        user.save()
        logout_from_all_devices(user.id, user.email)



def assign_admin_role(user):
    with transaction.atomic():
        user_role = UserRole.objects.create(user=user,role=Roles.objects.get(name="Admin"))
        user_role.save()
    return user_role

def assign_manager_role(user):
    with transaction.atomic():
        user_role = UserRole.objects.create(user=user,role=Roles.objects.get(name="Manager"))
        user_role.save()
    return user_role

def assign_patient_role(user):
    with transaction.atomic():
        user_role = UserRole.objects.create(user=user,role=Roles.objects.get(name="patient"))
        user_role.save()
    return user_role

