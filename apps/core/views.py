from django.contrib.contenttypes.models import ContentType
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core import simple_history

from . import pagination


class HistoryActionMixin:
    @swagger_auto_schema(
        operation_summary="History of an object",
        operation_description="Shows the history of the object.",
    )
    @action(detail=True, methods=["get"], name="Get Historical Records")
    def history(self, request, id):  # pylint: disable=unused-argument
        obj = self.get_object()
        history_list = simple_history.get_object_history_changes(obj)
        return Response(
            {"count": len(history_list), "results": history_list},
            status=status.HTTP_200_OK,
        )


class BaseModelViewSet(viewsets.ModelViewSet, HistoryActionMixin):
    lookup_field = "id"
    pagination_class = pagination.MainListPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data
        # Add additional data
        if isinstance(data, dict):
            # Get the model name and app label from serializer
            serializer_class = self.get_serializer_class()
            model_name = serializer_class.Meta.model._meta.model_name
            app_label = serializer_class.Meta.model._meta.app_label
            # Get content type from the model name and app label
            content_type = ContentType.objects.get(
                model=model_name, app_label=app_label
            )
            data["content_type"] = content_type.id
        return Response(data, status=status.HTTP_200_OK)


class BaseReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = "id"
    pagination_class = pagination.MainListPagination

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        data = response.data
        # Add additional data
        if isinstance(data, dict):
            # Get the model name and app label from serializer
            serializer_class = self.get_serializer_class()
            model_name = serializer_class.Meta.model._meta.model_name
            app_label = serializer_class.Meta.model._meta.app_label
            # Get content type from the model name and app label
            content_type = ContentType.objects.get(
                model=model_name, app_label=app_label
            )
            data["content_type"] = content_type.id
        return Response(data, status=status.HTTP_200_OK)
