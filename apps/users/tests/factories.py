import factory
from django.db.models.signals import post_save

from apps.core.faker import fake
from apps.users import models as mdl


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    password = fake.password()
    email = factory.Faker("ascii_email", locale="es_CO")
    is_active = fake.pybool()
    profile = factory.RelatedFactory(
        "apps.profiles.tests.factories.ProfileFactory",
        factory_related_name="user",
    )

    class Meta:
        model = mdl.User

    class Params:
        is_test = True
