from django.db import models


class SearchType(models.TextChoices):
    AUTOCOMPLETE = "autocomplete"
    FULL = "full"
