from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters as drf_filters

from apps.core.views import BaseModelViewSet
from apps.users import filters
from apps.users.api.v1 import serializers


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL
    client_class = OAuth2Client


@swagger_auto_schema(
    operation_summary="API for CRUD user",
    operation_description="This API is used for CRUD a user",
)
class UserViewSet(BaseModelViewSet):
    serializer_class = serializers.UserFormSerializer
    queryset = serializers.UserFormSerializer.Meta.model.objects.all()
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = filters.UserFilter
    search_fields = [
        "name",
        "first_name",
        "last_name",
        "email",
    ]

    @swagger_auto_schema(
        operation_summary="List all users",
        operation_description="This returns a list of all user objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a user",
        operation_description="This returns a created user object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a user",
        operation_description="This returns a user object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a user",
        operation_description="Update a user with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a user",
        operation_description="This returns partial updated the user object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a user",
        operation_description="This returns a deleted user object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
