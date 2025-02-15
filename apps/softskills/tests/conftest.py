from pytest_factoryboy import register

from apps.profiles.tests import factories as pro_factories

from . import factories

register(factories.SoftskillFactory)
register(factories.QuestionFactory)
register(factories.OptionFactory)
register(factories.QuestionnaireGroupFactory)
register(factories.QuestionnaireFactory)
register(factories.AnswerFactory)
register(factories.SoftskillTrainingFactory)
register(pro_factories.ProfileFactory)
