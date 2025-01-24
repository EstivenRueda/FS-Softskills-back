from rest_framework import serializers

from apps.core import serializers as core_serializers
from apps.files import enums, exceptions, models
from apps.files.constants import (
    ALLOWED_FILES,
    ALLOWED_IMAGES,
    UNIQUE_PER_SOURCE_CATEGORIES,
)


class FileSerializer(core_serializers.BaseModelSerializer):
    app_label = serializers.CharField(source="content_type.app_label", read_only=True)
    model = serializers.CharField(source="content_type.model", read_only=True)
    format = serializers.SerializerMethodField()

    class Meta:
        model = models.File
        fields = (
            "id",
            "source_id",
            "content_type",
            "app_label",
            "model",
            "name",
            "path",
            "category",
            "reference_link",
            "observations",
            "format",
            "is_active",
            "created_at",
        )

    def validate_path(self, value):
        if self.instance:
            category = self.instance.category
        else:
            category = self.initial_data.get("category")

        if category == enums.FileCategory.DOCUMENT and not value.name.lower().endswith(
            ALLOWED_FILES
        ):
            raise exceptions.InvalidDocumentFormatError(
                allowed_files=", ".join(ALLOWED_FILES)
            )
        elif category in [
            enums.FileCategory.LOGO,
            enums.FileCategory.PHOTO,
        ] and not value.name.lower().endswith(ALLOWED_IMAGES):
            raise exceptions.InvalidImageFormatError(
                allowed_images=", ".join(ALLOWED_IMAGES)
            )

        return value

    def get_format(self, obj):
        return obj.get_file_format().replace(".", "")

    def validate_category(self, value):
        # Get source_id and category object
        if self.instance:
            # If updating an existing record, retrieve the current category and source_id
            category = self.instance.category
            source_id = self.instance.source_id
        else:
            # If creating a new record, retrieve the category and source_id from the initial data
            category = self.initial_data.get("category")
            source_id = self.initial_data.get("source_id")

        # Check if the category is 'photo' or 'logo'
        if category in UNIQUE_PER_SOURCE_CATEGORIES:
            # If updating an existing record, exclude the current object from validation
            if self.instance:
                existing_files = models.File.objects.filter(
                    source_id=source_id, category=category
                ).exclude(id=self.instance.id)
            else:
                # If creating a new record, do not exclude any ID
                existing_files = models.File.objects.filter(
                    source_id=source_id, category=category
                )

            # If a file with the same source_id and category already exists, raise an error
            if existing_files.exists():
                raise exceptions.UniqueImageCategoryError(
                    categories="/".join(UNIQUE_PER_SOURCE_CATEGORIES)
                )

        return value

    def validate_name(self, value):
        # Get source_id and name object
        if self.instance:
            # If updating an existing record, retrieve the current name and source_id
            name = self.instance.name
            source_id = self.instance.source_id
        else:
            # If creating a new record, retrieve the name and source_id from the initial data
            name = self.initial_data.get("name")
            source_id = self.initial_data.get("source_id")

        # If updating an existing record, exclude the current object from validation
        if self.instance:
            existing_files = models.File.objects.filter(
                source_id=source_id, name=name
            ).exclude(id=self.instance.id)
        else:
            # If creating a new record, do not exclude any ID
            existing_files = models.File.objects.filter(source_id=source_id, name=name)

        # If a file with the same source_id and name already exists, raise an error
        if existing_files.exists():
            raise exceptions.DuplicateFileNameError(file_name=name)

        return value


class CategorySerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()
