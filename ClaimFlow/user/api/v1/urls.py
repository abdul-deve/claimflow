from django.urls import path ,include

from rest_framework.routers import DefaultRouter

from user.api.v1.views.user import UserViewSet

routers = DefaultRouter()
routers.register("auth",UserViewSet,basename="user")

urlpatterns = [
    path("",include(routers.urls))
]