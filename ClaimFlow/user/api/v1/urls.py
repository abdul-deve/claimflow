from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from user.api.v1.views.user import AuthViewSet,UserViewSet
routers = DefaultRouter()
routers.register("auth", AuthViewSet, basename="user_auth")
routers.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("",include(routers.urls)),
    path("jwt/refresh/",TokenRefreshView.as_view()),

]