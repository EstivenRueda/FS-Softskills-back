import crum
from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.core import managers, utils
from apps.users.models import User


class Activable(models.Model):
    is_active = models.BooleanField(
        verbose_name="is active",
        default=True,
    )

    class Meta:
        abstract = True


class Descriptable(models.Model):
    description = models.CharField(
        max_length=settings.DESCRIPTION_MAX_LENGTH,
        verbose_name="description",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.description:
            self.description = self.description.strip()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.description}"


class Nameable(models.Model):
    name = models.CharField(
        max_length=settings.NAME_MAX_LENGTH,
        verbose_name="name",
        db_index=True,
    )

    def save(self, *args, **kwargs):
        if self.name:
            self.name = utils.format_and_clean_str(self.name)
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name}"


class Orderable(models.Model):
    order = models.PositiveIntegerField(
        verbose_name="order",
        blank=True,
        null=True,
        help_text="Defines the default order for displaying items system-wide.",
    )

    class Meta:
        abstract = True
        ordering = ["order"]


class SoftDeletable(models.Model):
    """
    A Django model that will be marked as deleted, rather than actually removed from the database table, when delete()
    is called. Queries executed against this model will exclude soft-deleted objects.
    """

    deleted = models.BooleanField(default=False, blank=True, verbose_name="deleted")
    deleted_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True, verbose_name="deleted at"
    )
    deleted_by = models.ForeignKey(
        User,
        verbose_name="deleted by",
        related_name="%(app_label)s_%(class)s_deleted_by",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    deletion_ip = models.GenericIPAddressField(
        null=True, blank=True, verbose_name="deletion ip"
    )

    objects = managers.FilterDeletedObjectsManager()
    include_deleted_objects = models.Manager()

    def delete(self):  # pylint: disable=arguments-differ
        if hasattr(self, "deleted"):
            self.deleted = True
            self.save(update_fields=["deleted"])
        else:
            raise RuntimeError(f"Cannot soft-delete object of type {type(self)}")

    class Meta:
        abstract = True


class TimeStampable(SoftDeletable):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    created_by = models.ForeignKey(
        User,
        verbose_name="created by",
        related_name="%(app_label)s_%(class)s_create_by",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    creation_ip = models.GenericIPAddressField(
        null=True, blank=True, verbose_name="creation ip"
    )
    last_updated_at = models.DateTimeField(
        auto_now_add=False, null=True, blank=True, verbose_name="last update at"
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="updated by",
        related_name="%(app_label)s_%(class)s_updated_by",
    )
    update_ip = models.GenericIPAddressField(
        null=True, blank=True, verbose_name="update ip"
    )

    class Meta:
        abstract = True
        ordering = ["created_at", "updated_at"]

    def save(self, *args, **kwargs):
        current_request = crum.get_current_request()
        current_user = crum.get_current_user()
        if self._state.adding:
            self.created_at = timezone.now()
            if current_request:
                self.creation_ip = crum.get_current_request().META["REMOTE_ADDR"]
            if isinstance(current_user, User):
                self.created_by = crum.get_current_user()
        else:
            self.last_updated_at = timezone.now()
            if current_request:
                self.update_ip = crum.get_current_request().META["REMOTE_ADDR"]
            if isinstance(current_user, User):
                self.updated_by = crum.get_current_user()
        return super().save(*args, **kwargs)


class Observable(models.Model):
    observations = models.CharField(
        max_length=settings.OBSERVATIONS_MAX_LENGTH,
        verbose_name="observations",
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if self.observations:
            self.observations = self.observations.strip()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.observations}"
