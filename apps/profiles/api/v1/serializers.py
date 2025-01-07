from apps.core import serializers as core_serializers
from apps.profiles.models import Profile


class ProfileSerializer(core_serializers.BaseModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "display_name",
            "user",
            "type",
        ]
