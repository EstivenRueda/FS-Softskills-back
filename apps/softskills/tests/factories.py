import random

import factory

from apps.profiles import models as pro_mdl
from apps.profiles.tests.factories import ProfileFactory
from apps.softskills import enums
from apps.softskills import models as mdl


class SoftskillFactory(factory.django.DjangoModelFactory):
    name = factory.LazyAttribute(
        lambda _: random.choice(
            [
                "Gestión del estrés",
                "Resiliencia",
                "Proactividad",
            ]
        )
    )

    class Meta:
        model = mdl.Softskill

    class Params:
        is_test = True


class QuestionFactory(factory.django.DjangoModelFactory):
    softskill = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(SoftskillFactory),
        no_declaration=factory.Iterator(mdl.Softskill.objects.all()),
    )
    description = factory.Faker("text", max_nb_chars=100)
    order = factory.LazyAttribute(
        lambda _: random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    )

    class Meta:
        model = mdl.Question

    class Params:
        is_test = True


class OptionFactory(factory.django.DjangoModelFactory):
    question = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(QuestionFactory),
        no_declaration=factory.Iterator(mdl.Question.objects.all()),
    )
    option = factory.LazyAttribute(
        lambda _: random.choice(enums.LikertOptions.choices)[0]
    )
    grade = factory.LazyAttribute(lambda _: random.choice([1, 3, 5, 8, 10]))

    class Meta:
        model = mdl.Option

    class Params:
        is_test = True


class QuestionnaireGroupFactory(factory.django.DjangoModelFactory):
    attendee = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(ProfileFactory),
        no_declaration=factory.Iterator(pro_mdl.Profile.objects.all()),
    )

    class Meta:
        model = mdl.QuestionnaireGroup

    class Params:
        is_test = True


class QuestionnaireFactory(factory.django.DjangoModelFactory):
    questionnaire_group = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(QuestionnaireGroupFactory),
        no_declaration=factory.Iterator(mdl.QuestionnaireGroup.objects.all()),
    )
    softskill = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(SoftskillFactory),
        no_declaration=factory.Iterator(mdl.Softskill.objects.all()),
    )
    attendee = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(ProfileFactory),
        no_declaration=factory.Iterator(pro_mdl.Profile.objects.all()),
    )
    observations = factory.Faker("sentence", nb_words=8)

    class Meta:
        model = mdl.Questionnaire

    class Params:
        is_test = True


class AnswerFactory(factory.django.DjangoModelFactory):
    questionnaire = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(QuestionnaireFactory),
        no_declaration=factory.Iterator(mdl.Questionnaire.objects.all()),
    )
    question = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(QuestionFactory),
        no_declaration=factory.Iterator(mdl.Question.objects.all()),
    )
    option = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(OptionFactory),
        no_declaration=factory.Iterator(mdl.Option.objects.all()),
    )
    observations = factory.Faker("sentence", nb_words=8)

    class Meta:
        model = mdl.Answer

    class Params:
        is_test = True


class SoftskillTrainingFactory(factory.django.DjangoModelFactory):
    softskill = factory.Maybe(
        "is_test",
        yes_declaration=factory.SubFactory(SoftskillFactory),
        no_declaration=factory.Iterator(mdl.Softskill.objects.all()),
    )
    title = factory.Faker("sentence", nb_words=5)
    description = factory.Faker("text", max_nb_chars=100)
    link = factory.Faker("url")
    min_grade = factory.LazyAttribute(lambda _: random.choice([0, 25, 50, 75]))
    max_grade = factory.LazyAttribute(lambda o: o.min_grade + 25)

    class Meta:
        model = mdl.SoftskillTraining

    class Params:
        is_test = True
