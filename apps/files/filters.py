import django_filters

from apps.files import models as mdl


class FileFilter(django_filters.FilterSet):
    is_active = django_filters.BooleanFilter()
    source_id = django_filters.CharFilter(
        field_name="source_id",
        lookup_expr="exact",
        label="source_id",
    )
    name = django_filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="name",
    )
    content_type_id = django_filters.CharFilter(
        field_name="content_type",
        lookup_expr="exact",
        label="content_type_id",
    )

    class Meta:
        model = mdl.File
        fields = [
            "is_active",
            "source_id",
            "name",
            "content_type_id",
        ]
