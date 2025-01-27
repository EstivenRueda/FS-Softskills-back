from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters as drf_filters
from rest_framework import views
from rest_framework.response import Response

from apps.core.views import BaseModelViewSet
from apps.profiles import enums, filters
from apps.profiles.api.v1 import serializers


@swagger_auto_schema(
    operation_summary="API for CRUD profile",
    operation_description="This API is used for CRUD a profile",
)
class ProfileViewSet(BaseModelViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = serializers.ProfileSerializer.Meta.model.objects.all()
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = filters.ProfileFilter
    search_fields = [
        "display_name",
        "user__first_name",
        "user__last_name",
    ]

    @swagger_auto_schema(
        operation_summary="List all profiles",
        operation_description="This returns a list of all profile objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a profile",
        operation_description="This returns a created profile object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a profile",
        operation_description="This returns a profile object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a profile",
        operation_description="Update a profile with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a profile",
        operation_description="This returns partial updated the profile object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a profile",
        operation_description="This returns a deleted profile object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for list all profile types",
    operation_description="This API is used to list all profile types",
)
class ProfileTypesAPIView(views.APIView):
    @swagger_auto_schema(
        operation_summary="List all profile types",
        operation_description="This returns a list of all profile type objects",
    )
    def get(self, request):
        profile_type_choices = enums.ProfileType.choices
        profile_type_serializer = serializers.ProfileTypeSerializer(
            [
                {"value": value, "display_name": display_name}
                for value, display_name in profile_type_choices
            ],
            many=True,
        )

        return Response(profile_type_serializer.data)
