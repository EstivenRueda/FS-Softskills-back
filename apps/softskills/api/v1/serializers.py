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
    questionnaire = serializers.UUIDField(required=False, source="questionnaire.id")
    question_obj = QuestionSerializer(read_only=True)
    option_obj = OptionSerializer(read_only=True)

    class Meta:
        model = models.Answer
        fields = (
            "id",
            "questionnaire",
            "question",
            "question_obj",
            "option",
            "option_obj",
            "grade",
        )


class QuestionnaireSerializer(WritableNestedModelSerializer):
    softskill_name = serializers.CharField(source="softskill.name", read_only=True)
    attendee_name = serializers.CharField(
        source="attendee.display_name", read_only=True
    )
    answers = AnswerSerializer(required=False, many=True)
    attendee = serializers.UUIDField(required=False, source="attendee.id")

    class Meta:
        model = models.Questionnaire
        fields = (
            "id",
            "softskill",
            "softskill_name",
            "attendee",
            "attendee_name",
            "is_current",
            "observations",
            "grade",
            "is_active",
            "answers",
        )

    def create(self, validated_data):
        questionnaire = super().create(validated_data)

        # Update the questionnaire grade
        questionnaire.save()
        return questionnaire

    def update(self, instance, validated_data):
        questionnaire = super().update(instance, validated_data)

        # Update the questionnaire grade
        questionnaire.save()
        return questionnaire


class QuestionnaireResultsSerializer(WritableNestedModelSerializer):
    softskill_name = serializers.CharField(source="softskill.name", read_only=True)
    attendee_name = serializers.CharField(
        source="attendee.display_name", read_only=True
    )

    class Meta:
        model = models.Questionnaire
        fields = (
            "id",
            "softskill",
            "softskill_name",
            "attendee",
            "attendee_name",
            "is_current",
            "observations",
            "grade",
            "is_active",
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
            "min_grade",
            "max_grade",
            "is_active",
        )
