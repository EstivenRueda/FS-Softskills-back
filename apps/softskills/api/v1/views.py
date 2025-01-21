from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters as drf_filters
from rest_framework import views
from rest_framework.response import Response

from apps.core.views import BaseModelViewSet
from apps.softskills import enums, filters
from apps.softskills.api.v1 import serializers


@swagger_auto_schema(
    operation_summary="API for CRUD a softskill",
    operation_description="This API is used for CRUD a softskill",
)
class SoftskillViewSet(BaseModelViewSet):
    lookup_field = "slug"
    queryset = serializers.SoftskillSerializer.Meta.model.objects.all()
    serializer_class = serializers.SoftskillSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = filters.SoftskillFilter
    search_fields = ["name"]

    @swagger_auto_schema(
        operation_summary="List all softskills",
        operation_description="This returns a list of all softskill objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a softskill",
        operation_description="This returns a created softskill object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a softskill",
        operation_description="This returns a softskill object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a softskill",
        operation_description="Update a softskill with the slug",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a softskill",
        operation_description="This returns partial updated the softskill object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a softskill",
        operation_description="This returns a deleted softskill object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for CRUD a question",
    operation_description="This API is used for CRUD a question",
)
class QuestionViewSet(BaseModelViewSet):
    queryset = serializers.QuestionSerializer.Meta.model.objects.all()
    serializer_class = serializers.QuestionSerializer
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter]
    filterset_class = filters.QuestionFilter
    search_fields = ["description"]

    @swagger_auto_schema(
        operation_summary="List all questions",
        operation_description="This returns a list of all question objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a question",
        operation_description="This returns a created question object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a question",
        operation_description="This returns a question object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a question",
        operation_description="Update a question with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a question",
        operation_description="This returns partial updated the question object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a question",
        operation_description="This returns a deleted question object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for list all likert options",
    operation_description="This API is used to list all likert options",
)
class LikertOptionAPIView(views.APIView):
    @swagger_auto_schema(
        operation_summary="List all likert options",
        operation_description="This returns a list of all likert option objects",
    )
    def get(self, request):
        likert_option_choices = enums.LikertOptions.choices
        likert_option_serializer = serializers.LikertOptionSerializer(
            [
                {"value": value, "display_name": display_name}
                for value, display_name in likert_option_choices
            ],
            many=True,
        )

        return Response(likert_option_serializer.data)


@swagger_auto_schema(
    operation_summary="API for CRUD a option",
    operation_description="This API is used for CRUD a option",
)
class OptionViewSet(BaseModelViewSet):
    queryset = serializers.OptionSerializer.Meta.model.objects.all()
    serializer_class = serializers.OptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.OptionFilter

    @swagger_auto_schema(
        operation_summary="List all options",
        operation_description="This returns a list of all option objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a option",
        operation_description="This returns a created option object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a option",
        operation_description="This returns a option object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a option",
        operation_description="Update a option with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a option",
        operation_description="This returns partial updated the option object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a option",
        operation_description="This returns a deleted option object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for CRUD a questionnaire",
    operation_description="This API is used for CRUD a questionnaire",
)
class QuestionnaireViewSet(BaseModelViewSet):
    queryset = serializers.QuestionnaireSerializer.Meta.model.objects.all()
    serializer_class = serializers.QuestionnaireSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.QuestionnaireFilter

    @swagger_auto_schema(
        operation_summary="List all questionnaires",
        operation_description="This returns a list of all questionnaire objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a questionnaire",
        operation_description="This returns a created questionnaire object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a questionnaire",
        operation_description="This returns a questionnaire object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a questionnaire",
        operation_description="Update a questionnaire with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a questionnaire",
        operation_description="This returns partial updated the questionnaire object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a questionnaire",
        operation_description="This returns a deleted questionnaire object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for CRUD an answer",
    operation_description="This API is used for CRUD an answer",
)
class AnswerViewSet(BaseModelViewSet):
    queryset = serializers.AnswerSerializer.Meta.model.objects.all()
    serializer_class = serializers.AnswerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.AnswerFilter

    @swagger_auto_schema(
        operation_summary="List all answers",
        operation_description="This returns a list of all answer objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create an answer",
        operation_description="This returns a created answer object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get an answer",
        operation_description="This returns an answer object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an answer",
        operation_description="Update an answer with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update an answer",
        operation_description="This returns partial updated the answer object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an answer",
        operation_description="This returns a deleted answer object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


@swagger_auto_schema(
    operation_summary="API for CRUD a softskill training",
    operation_description="This API is used for CRUD a softskill training",
)
class SoftskillTrainingViewSet(BaseModelViewSet):
    queryset = serializers.SoftskillTrainingSerializer.Meta.model.objects.all()
    serializer_class = serializers.SoftskillTrainingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.SoftskillTrainingFilter

    @swagger_auto_schema(
        operation_summary="List all softskill trainings",
        operation_description="This returns a list of all softskill training objects",
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a softskill training",
        operation_description="This returns a created softskill training object",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Get a softskill training",
        operation_description="This returns a softskill training object",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a softskill training",
        operation_description="Update a softskill training with the ID",
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a softskill training",
        operation_description="This returns partial updated the softskill training object",
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a softskill training",
        operation_description="This returns a deleted softskill training object",
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
