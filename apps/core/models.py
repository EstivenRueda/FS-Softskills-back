import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    idx = models.BigIntegerField(default=1)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"<{self.__class__.__qualname__}: id='{self.id}'>"

    def save(self, *args, **kwargs):
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_idx = self.__class__.objects.all().aggregate(
                largest=models.Max("idx")
            )["largest"]

            if last_idx is not None:
                self.idx = last_idx + 1

        super().save(*args, **kwargs)


class BasePermissionModel(models.Model):
    class Meta:
        abstract = True
        default_permissions = ()
