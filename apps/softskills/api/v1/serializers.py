from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from apps.core import serializers as core_serializers
from apps.softskills import models


class SoftskillSerializer(core_serializers.BaseModelSerializer):
    slug = serializers.CharField(required=False)

    class Meta:
        model = models.Softskill
        fields = (
            "id",
            "name",
            "slug",
            "is_active",
        )


class LikertOptionSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()


class OptionSerializer(core_serializers.BaseModelSerializer):
    question = serializers.UUIDField(required=False, source="question.id")
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Option
        fields = (
            "id",
            "question",
            "option",
            "grade",
            "display_name",
        )

    def get_display_name(self, obj):
        return obj.get_option_display()


class QuestionSerializer(WritableNestedModelSerializer):
    softskill_name = serializers.CharField(source="softskill.name", read_only=True)
    options = OptionSerializer(required=False, many=True)

    class Meta:
        model = models.Question
        fields = (
            "id",
            "description",
            "order",
            "softskill",
            "softskill_name",
            "is_active",
            "options",
        )


class AnswerSerializer(core_serializers.BaseModelSerializer):
    question = QuestionSerializer(read_only=True)
    option = OptionSerializer(read_only=True)

    class Meta:
        model = models.Answer
        fields = (
            "id",
            "questionnaire",
            "question",
            "option",
            "grade",
        )


class QuestionnaireSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(required=False, many=True)

    class Meta:
        model = models.Questionnaire
        fields = (
            "id",
            "softskill",
            "attendee",
            "is_current",
            "observations",
            "grade",
            "is_active",
            "answers",
        )


class SoftskillTrainingSerializer(core_serializers.BaseModelSerializer):
    softskill_name = serializers.CharField(source="softskill.name", read_only=True)

    class Meta:
        model = models.SoftskillTraining
        fields = (
            "id",
            "softskill",
            "softskill_name",
            "title",
            "description",
            "link",
            "min_range",
            "max_range",
            "is_active",
        )
