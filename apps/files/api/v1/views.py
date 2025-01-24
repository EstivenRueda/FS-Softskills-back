from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters as drf_filters
from rest_framework import views
from rest_framework.response import Response

from apps.core.views import BaseModelViewSet
from apps.files import enums, filters
from apps.files.api.v1 import serializers


@swagger_auto_schema(
    operation_summary="API for CRUD a file document",
    operation_description="This API is used for CRUD a file document",
)
class FileViewSet(BaseModelViewSet):
    serializer_class = serializers.FileSerializer
    queryset = serializers.FileSerializer.Meta.model.objects.all()
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = filters.FileFilter
    search_fields = [
        "name",
    ]

    @swagger_auto_schema(
        operation_summary="Update a file document",
        operation_description="Update a file document with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a file document",
        operation_description="This returns a file document object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a file document",
        operation_description="This returns a created file document object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="List all file documents",
        operation_description="This returns a list of all file document objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a file document",
        operation_description="This returns a deleted file document object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a file document",
        operation_description="This returns partial updated the file document object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for list all file category options of a file",
    operation_description="This API is used for list all file category options of a file",
)
class CategoryAPIView(views.APIView):
    @swagger_auto_schema(
        operation_summary="List all file category options",
        operation_description="This returns a list of all file category objects",
    )
    def get(self, request):
        category_choices = enums.FileCategory.choices
        category_serializer = serializers.CategorySerializer(
            [
                {"value": value, "display_name": display_name}
                for value, display_name in category_choices
            ],
            many=True,
        )

        return Response(category_serializer.data)
