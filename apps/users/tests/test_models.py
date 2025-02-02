import pytest

from apps.profiles import enums as pro_enums
from apps.profiles import models as pro_mdl
from apps.users import models as mdl


@pytest.mark.unit
@pytest.mark.django_db
class TestUserModel:
    def test_create_user_successfully(self):
        mdl.User.objects.create(
            password="f1n1sh1n6Sch00l",
            name="Estiven",
            email="testemail@example.com",
        )

        assert mdl.User.objects.count() >= 1

    def test_create_user_and_profile_successfully(self):
        user = mdl.User.objects.create(
            password="f1n1sh1n6Sch00l",
            name="Estiven",
            email="testemail@example.com",
        )

        assert mdl.User.objects.count() >= 1

        assert pro_mdl.Profile.objects.count() >= 1

        profile = pro_mdl.Profile.objects.filter(user=user).first()

        assert profile.display_name == user.name
        assert profile.type == pro_enums.ProfileType.STUDENT
        assert profile.user == user
