from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.files.api.v1 import views

router = DefaultRouter()

router.register(r"files", views.FileViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("categories/", views.CategoryAPIView.as_view(), name="categories"),
]
