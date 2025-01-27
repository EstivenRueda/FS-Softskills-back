import uuid

import crum
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from apps.core.logging import get_finishing_school_logging

logger = get_finishing_school_logging(__name__)


# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    name = models.CharField("Nombre", max_length=150, blank=True)
    last_login_ip = models.GenericIPAddressField(
        null=True, blank=True, verbose_name="Ultimo IP login"
    )
    password_reset_timestamp = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def save(
        self,
        *args,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.name = f"{self.first_name} {self.last_name}"
        return super().save(force_insert, force_update, using, update_fields)

    def _update_last_login_ip(self, *args, **kwargs):
        try:
            request = crum.get_current_request()
            if request is None:
                return None

            # Try first to get the IP from X-Forwarded-For
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                ip = x_forwarded_for.split(",")[0].strip()  # Take the first IP
            else:
                # Use REMOTE_ADDR as fallback
                ip = request.META.get("REMOTE_ADDR")

            self.last_login_ip = ip
            self.last_login = timezone.now()
            self.save()
        except Exception as e:
            logger.exception(e)

    def create_user_profile(self):
        """
        Creates a user profile if it does not already exist.

        Checks if the current user instance has an associated profile. If not, it creates a new profile.
        The display name for the profile is set to the user's name if available, otherwise to the user's email.
        The profile type is set to 'STUDENT'.
        """
        from apps.profiles import enums as pro_enums
        from apps.profiles.models import Profile

        if not hasattr(self, "profile"):
            Profile.objects.create(
                user=self,
                display_name=self.name or self.email,
                type=pro_enums.ProfileType.STUDENT,
            )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a user profile after a User instance is created.
    """
    if created:
        instance.create_user_profile()
