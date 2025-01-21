from django.db import models
from simple_history.models import HistoricalRecords

from apps.core import behaviors as bhs
from apps.core import models as core_models
from apps.profiles import enums, managers, querysets
from apps.users.models import User


class Profile(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Activable,
):
    """
    This model represents a user profile.
    It inherits from BaseModel, TimeStampable, and Activable, providing core functionalities,
    timestamping, and activation status, respectively.

    Fields:
        display_name: The display name of the profile.
        user: A one-to-one relationship with the User model.
        type: The type of profile, chosen from a predefined set of choices.
        history: A field to enable tracking historical changes.
        objects: A custom manager to handle queryset operations for the Profile model.
    """

    display_name = models.CharField(
        verbose_name="display_name",
        max_length=100,
    )
    user = models.OneToOneField(
        User,
        verbose_name="user",
        on_delete=models.PROTECT,
        related_name="profile",
    )
    type = models.CharField(
        max_length=30,
        choices=enums.ProfileType.choices,
        verbose_name="type",
    )
    objects = managers.ProfileManager.from_queryset(querysets.ProfileQuerySet)()
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering = [
            "-is_active",
            "-created_at",
        ]

    def __str__(self) -> str:
        return f"{self.display_name} - {self.type}"
