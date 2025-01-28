import crum
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from simple_history.models import HistoricalRecords

from apps.core import behaviors as bhs
from apps.core import models as core_models
from apps.profiles.models import Profile
from apps.users.models import User

from . import enums


class Softskill(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Nameable,
    bhs.Activable,
):
    """
    This model represents a softskill.
    It inherits from BaseModel, TimeStampable, Nameable and Activable, providing core functionalities,
    timestamping, naming and activation status, respectively.

    Fields:
        slug: A slug to identify the softskill in the URL.
        history: A field to enable tracking historical changes.
    """

    slug = models.SlugField(
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        db_index=True,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Habilidad Blanda"
        verbose_name_plural = "Habilidades Blandas"
        ordering = [
            "-is_active",
            "created_at",
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Question(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Activable,
    bhs.Descriptable,
    bhs.Orderable,
):
    """
    This model represents a question.
    It inherits from BaseModel, TimeStampable, Activable, Descriptable and Orderable
    providing core functionalities.

    Fields:
        softskill: A foreign key relationship to the `Softskill` model.
        history: A field to enable tracking historical changes.
    """

    softskill = models.ForeignKey(
        Softskill,
        verbose_name="softskill",
        on_delete=models.PROTECT,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = [
            "order",
            "-is_active",
            "-created_at",
        ]


class Option(
    core_models.BaseModel,
    bhs.TimeStampable,
):
    """
    This model represents an opction to answer.
    It inherits from BaseModel and TimeStampable
    providing core functionalities.

    Fields:
        question: A foreign key relationship to the `Question` model.
        option: One of the likert options.
        history: A field to enable tracking historical changes.
    """

    question = models.ForeignKey(
        Question,
        verbose_name="question",
        related_name="options",
        on_delete=models.PROTECT,
    )
    option = models.CharField(
        verbose_name="option",
        max_length=20,
        choices=enums.LikertOptions.choices,
    )
    grade = models.PositiveIntegerField(
        verbose_name="grade",
    )


class QuestionnaireGroup(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Activable,
):
    attendee = models.ForeignKey(
        Profile,
        related_name="questionnaire_groups",
        verbose_name="attendee",
        on_delete=models.PROTECT,
    )
    is_current = models.BooleanField(
        verbose_name="is current",
        default=True,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Grupo de cuestionarios"
        verbose_name_plural = "Grupos de cuestionarios"
        ordering = [
            "-is_active",
            "-created_at",
        ]

    def save(self, *args, **kwargs):
        current_user = crum.get_current_user()
        if self._state.adding:
            if isinstance(current_user, User):
                self.attendee = current_user.profile

            QuestionnaireGroup.objects.filter(
                attendee=self.attendee, is_current=True
            ).update(is_current=False)

        super().save(*args, **kwargs)


class Questionnaire(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Activable,
):
    """
    This model represents a questionnaire.
    It inherits from BaseModel, TimeStampable and Activable
    providing core functionalities.

    Fields:
        softskill: A foreign key relationship to the `Softskill` model.
        attendee: A foreign key relationship to the `Profile` model.
        is_current: A field to determine wether the questionnaire is current or not.
        observations: Observations to the questionnaire.
        grade: Final grade of the questionnaire.
        history: A field to enable tracking historical changes.
    """

    questionnaire_group = models.ForeignKey(
        QuestionnaireGroup,
        related_name="questionnaires",
        verbose_name="questionnaire group",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
    )

    softskill = models.ForeignKey(
        Softskill,
        verbose_name="softskill",
        on_delete=models.PROTECT,
    )
    attendee = models.ForeignKey(
        Profile,
        related_name="attendee_questionnaire",
        verbose_name="attendee",
        on_delete=models.PROTECT,
    )
    is_current = models.BooleanField(
        verbose_name="is current",
        default=True,
    )
    observations = models.TextField(
        verbose_name="observations",
        blank=True,
        null=True,
        default="",
    )
    grade = models.PositiveIntegerField(
        verbose_name="grade",
        blank=True,
        null=False,
        default=0,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Cuestionario"
        verbose_name_plural = "Cuestionarios"
        ordering = [
            "-is_active",
            "-created_at",
        ]

    def save(self, *args, **kwargs):
        current_user = crum.get_current_user()
        if self._state.adding:
            if isinstance(current_user, User):
                self.attendee = current_user.profile

            Questionnaire.objects.filter(
                attendee=self.attendee, softskill=self.softskill, is_current=True
            ).update(is_current=False)

        total_grade = self.answers.aggregate(total=models.Sum("grade"))["total"] or 0
        self.grade = total_grade
        super().save(*args, **kwargs)


class Answer(
    core_models.BaseModel,
    bhs.TimeStampable,
):
    """
    This model represents an answer.
    It inherits from BaseModel, TimeStampable and Activable
    providing core functionalities.

    Fields:
        questionnaire: A foreign key relationship to the `Questionnaire` model.
        question: A foreign key relationship to the `Question` model.
        option: A foreign key relationship to the `Option` model.
        grade: Final grade of the questionnaire.
        history: A field to enable tracking historical changes.
    """

    questionnaire = models.ForeignKey(
        Questionnaire,
        verbose_name="questionnaire",
        related_name="answers",
        on_delete=models.PROTECT,
    )
    question = models.ForeignKey(
        Question,
        verbose_name="question",
        on_delete=models.PROTECT,
    )
    option = models.ForeignKey(
        Option,
        verbose_name="option",
        on_delete=models.PROTECT,
    )
    grade = models.PositiveIntegerField(
        verbose_name="grade",
        blank=True,
        null=False,
        default=0,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        self.grade = self.option.grade
        return super().save(*args, **kwargs)


class SoftskillTraining(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Descriptable,
    bhs.Activable,
):
    """
    This model represents a training for a softskill.
    It inherits from BaseModel, TimeStampable, Descriptable and Activable
    providing core functionalities.

    Fields:
        softskill: A foreign key relationship to the `Softskill` model.
        title: The title of the training item.
        link: A foreign key relationship to the `Option` model.
        grade: Final grade of the questionnaire.
        history: A field to enable tracking historical changes.
    """

    softskill = models.ForeignKey(
        Softskill,
        verbose_name="softskill",
        on_delete=models.PROTECT,
    )
    title = models.CharField(
        verbose_name="title",
        max_length=150,
    )
    link = models.CharField(
        verbose_name="link",
        max_length=255,
    )
    min_grade = models.PositiveIntegerField(
        verbose_name="min grade",
        default=0,
    )
    max_grade = models.PositiveIntegerField(
        verbose_name="max grade",
        default=0,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Capacitación"
        verbose_name_plural = "Capacitaciones"
        ordering = [
            "-is_active",
            "-created_at",
        ]
