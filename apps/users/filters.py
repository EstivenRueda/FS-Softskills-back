import django_filters
from django.contrib.auth import get_user_model

from apps.profiles import enums

User = get_user_model()


class UserFilter(django_filters.FilterSet):
    profile_type = django_filters.ChoiceFilter(choices=enums.ProfileType.choices)
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = User
        fields = ["profile_type", "is_active"]
