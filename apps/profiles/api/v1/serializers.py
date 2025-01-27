from rest_framework import serializers

from apps.core import serializers as core_serializers
from apps.profiles.models import Profile


class ProfileSerializer(core_serializers.BaseModelSerializer):
    display_name = serializers.CharField(required=False)
    user = serializers.UUIDField(source="user_id", required=False)
    type_name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "display_name",
            "user",
            "type",
            "type_name",
        ]

    def get_type_name(self, obj):
        return obj.get_type_display()


class ProfileTypeSerializer(serializers.Serializer):
    value = serializers.CharField()
    display_name = serializers.CharField()
