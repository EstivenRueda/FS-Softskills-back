from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(UserDetailsSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            "id",
            "email",
            "name",
            "last_login",
            "permissions",
            "is_staff",
        )
        read_only_fields = (
            "id",
            "email",
            "last_login",
            "is_staff",
        )

    def get_permissions(self, user):
        return user.get_all_permissions()


class LoginSerializer(BaseLoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        user = attrs["user"]
        user._update_last_login_ip()
        attrs["user"] = user
        return attrs
