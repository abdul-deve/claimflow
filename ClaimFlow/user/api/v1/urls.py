from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.api.v1.views.user_auth import AuthViewSet
from user.api.v1.views.users import UserViewSet
routers = DefaultRouter()
routers.register("auth", AuthViewSet, basename="user_auth")
routers.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("",include(routers.urls)),

]