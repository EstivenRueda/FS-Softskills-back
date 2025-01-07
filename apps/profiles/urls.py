from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.profiles.api.v1 import views

router = DefaultRouter()

router.register(r"profiles", views.ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
