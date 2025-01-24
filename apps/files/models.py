import os

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

from apps.core import behaviors as bhs
from apps.core import models as core_models
from apps.core.logging import get_finishing_school_logging
from apps.files import enums, validators

logger = get_finishing_school_logging(__name__)


def file_upload_path(instance, filename):
    # Get the content_type attributes from validated data
    content_type = instance.content_type

    # Define the folder where the file will be saved
    folder = f"{content_type.app_label}/{content_type.model}"

    # Define the folder path where the file will be saved
    folder_path = f"files/{folder}/"

    # Build the complete file path within the specified folder
    new_route = os.path.join(folder_path, filename)
    logger.info(f"New file generated path: {new_route}")

    return new_route.replace("\\", "/")


class File(
    core_models.BaseModel,
    bhs.TimeStampable,
    bhs.Activable,
    bhs.Nameable,
    bhs.Observable,
):
    """
    A model that represents an attachment in certain system modules.

    Fields:
        name: A CharField representing the name of the file, with a maximum length of 255 characters.
        path: A field representing the file path.
        source_id: A field representing the source identifier.
        content_type: A foreign key relationship to the `ContentType` model.
        category: A field representing the category of the file, chosen from a
            predefined set of choices.
        reference_link: A field representing an optional reference link, with a maximum length of 200 characters.
        history: A historical record of changes made to instances of this model.

    """

    name = models.CharField(
        max_length=255,
        verbose_name=_("name"),
        db_index=True,
    )
    path = models.FileField(
        upload_to=file_upload_path,
        validators=[
            validators.validate_file_size,
            validators.validate_file_path_length,
        ],
        max_length=200,
    )
    source_id = models.UUIDField(
        verbose_name=_("source_id"),
    )
    content_type = models.ForeignKey(
        ContentType,
        verbose_name=_("content_type"),
        on_delete=models.PROTECT,
    )
    category = models.CharField(
        max_length=30,
        verbose_name=_("category"),
        choices=enums.FileCategory.choices,
    )
    reference_link = models.URLField(
        max_length=200,
        verbose_name=_("reference_link"),
        blank=True,
        null=True,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = _("file")
        verbose_name_plural = _("files")
        ordering = [
            "-is_active",
            "-created_at",
            "source_id",
        ]

    def __str__(self) -> str:
        return f"{self.name}"

    def get_file_format(self):
        """
        This method extracts and returns the file extension of the file associated with the `path`
        attribute of the instance.
        The file extension is returned in lower case.
        """
        _, file_extension = os.path.splitext(self.path.name)
        return file_extension.lower()
