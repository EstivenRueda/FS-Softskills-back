import random

import factory
from django.db.models.signals import post_save

from apps.profiles import enums
from apps.profiles import models as mdl
from apps.users.models import User
from apps.users.tests import factories as usr_factories


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(usr_factories.UserFactory, profile=None),
        no_declaration=factory.Iterator(User.objects.all()),
    )
    display_name = factory.Faker("user_name", locale="es_CO")
    type = factory.LazyAttribute(lambda _: random.choice(enums.ProfileType.choices)[0])

    class Meta:
        model = mdl.Profile

    class Params:
        is_test = True
