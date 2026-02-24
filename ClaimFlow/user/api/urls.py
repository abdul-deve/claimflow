from django.urls import path,include

urlpatterns = [
    path("", include("user.api.v1.urls")),
]