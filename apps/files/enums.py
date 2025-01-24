from django.db import models


class FileCategory(models.TextChoices):
    DOCUMENT = "DOCUMENT", "Documento"
    LOGO = "LOGO", "Logo"
    PHOTO = "PHOTO", "Photo"
