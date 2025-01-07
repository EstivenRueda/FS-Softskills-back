import django_filters

from . import enums
from .models import Profile


class ProfileFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(choices=enums.ProfileType.choices)
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Profile
        fields = ["type", "is_active"]
