from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model
from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from apps.profiles.api.v1.serializers import ProfileSerializer

User = get_user_model()


class UserSerializer(UserDetailsSerializer):
    permissions = serializers.SerializerMethodField()
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "last_login",
            "permissions",
            "is_staff",
            "profile",
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


class UserFormSerializer(WritableNestedModelSerializer):
    profile = ProfileSerializer()
    password = serializers.CharField(write_only=True, required=False)
    password_confirm = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "name",
            "is_active",
            "profile",
            "password",
            "password_confirm",
        )

    def validate(self, data):
        if "password" in data and "password_confirm" in data:
            if data["password"] != data["password_confirm"]:
                raise serializers.ValidationError(
                    {"password_confirm": "Las contraseñas no coinciden."}
                )
        return data

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        password_confirm = validated_data.pop("password_confirm", None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        password_confirm = validated_data.pop("password_confirm", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
