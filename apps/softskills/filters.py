import django_filters

from apps.softskills import models


class SoftskillFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter(
        field_name="is_active",
        lookup_expr="exact",
        label="is_active",
    )

    class Meta:
        model = models.Softskill
        fields = ["is_active"]


class QuestionFilter(django_filters.FilterSet):
    softskill_id = django_filters.CharFilter(
        field_name="softskill",
        lookup_expr="exact",
        label="softskill_id",
    )
    softskill_slug = django_filters.CharFilter(
        field_name="softskill__slug",
        lookup_expr="exact",
        label="softskill_slug",
    )
    is_active = django_filters.BooleanFilter(
        field_name="is_active",
        lookup_expr="exact",
        label="is_active",
    )

    class Meta:
        model = models.Question
        fields = [
            "softskill_id",
            "softskill_slug",
            "is_active",
        ]


class OptionFilter(django_filters.FilterSet):
    question_id = django_filters.CharFilter(
        field_name="question",
        lookup_expr="exact",
        label="question_id",
    )

    class Meta:
        model = models.Option
        fields = ["question_id"]


class QuestionnaireFilter(django_filters.FilterSet):
    softskill_id = django_filters.CharFilter(
        field_name="softskill",
        lookup_expr="exact",
        label="softskill_id",
    )
    attendee_id = django_filters.CharFilter(
        field_name="attendee",
        lookup_expr="exact",
        label="attendee_id",
    )
    is_current = django_filters.BooleanFilter(
        field_name="is_current",
        lookup_expr="exact",
        label="is_current",
    )
    is_active = django_filters.BooleanFilter(
        field_name="is_active",
        lookup_expr="exact",
        label="is_active",
    )

    class Meta:
        model = models.Questionnaire
        fields = [
            "softskill_id",
            "attendee_id",
            "is_current",
            "is_active",
        ]


class AnswerFilter(django_filters.FilterSet):
    questionnaire_id = django_filters.CharFilter(
        field_name="questionnaire",
        lookup_expr="exact",
        label="questionnaire_id",
    )

    class Meta:
        model = models.Answer
        fields = [
            "questionnaire_id",
        ]


class SoftskillTrainingFilter(django_filters.FilterSet):
    softskill_id = django_filters.CharFilter(
        field_name="softskill",
        lookup_expr="exact",
        label="softskill_id",
    )
    softskill_slug = django_filters.CharFilter(
        field_name="softskill__slug",
        lookup_expr="exact",
        label="softskill_slug",
    )
    is_active = django_filters.BooleanFilter(
        field_name="is_active",
        lookup_expr="exact",
        label="is_active",
    )

    class Meta:
        model = models.SoftskillTraining
        fields = [
            "softskill_id",
            "softskill_slug",
            "is_active",
        ]
