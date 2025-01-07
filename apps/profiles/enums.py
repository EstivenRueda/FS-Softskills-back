from django.db import models


class ProfileType(models.TextChoices):
    STUDENT = "STUDENT", "ESTUDIANTE"
    ADMINISTRATIVE = "ADMINISTRATIVE", "ADMINISTRATIVO"
