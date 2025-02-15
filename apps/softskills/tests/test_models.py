import pytest

from apps.softskills import enums
from apps.softskills import models as mdl


@pytest.mark.unit
@pytest.mark.django_db
class TestSoftskillModel:
    def test_create_softskill_successfully(self):
        mdl.Softskill.objects.create(name="Actitud positiva")
        assert mdl.Softskill.objects.count() >= 1

    def test_update_softskill_successfully(self, softskill):
        assert not softskill.name == "Inteligencia"
        softskill.name = "Inteligencia"
        softskill.save()
        updated_softskill = mdl.Softskill.objects.get(pk=softskill.id)
        assert updated_softskill.name == "Inteligencia"

    def test_delete_softskill_successfully(self, softskill):
        before_count = mdl.Softskill.objects.count()
        assert before_count >= 1
        softskill.delete()
        assert mdl.Softskill.objects.count() < before_count

    def test_softskill_change_history_created_successfully(self, softskill):
        softskill.name = "New Name"
        softskill.save()

        history = softskill.history.all()
        assert len(history) == 2


@pytest.mark.unit
@pytest.mark.django_db
class TestQuestionModel:
    def test_create_question_successfully(self, softskill):
        mdl.Question.objects.create(softskill=softskill)
        assert mdl.Question.objects.count() >= 1

    def test_update_question_successfully(self, question):
        assert not question.description == "New Description"
        question.description = "New Description"
        question.save()
        updated_question = mdl.Question.objects.get(pk=question.id)
        assert updated_question.description == "New Description"

    def test_delete_question_successfully(self, question):
        before_count = mdl.Question.objects.count()
        assert before_count >= 1
        question.delete()
        assert mdl.Question.objects.count() < before_count

    def test_question_change_history_created_successfully(self, question):
        question.description = "New Description"
        question.save()

        history = question.history.all()
        assert len(history) == 2


@pytest.mark.unit
@pytest.mark.django_db
class TestOptionModel:
    def test_create_option_successfully(self, question):
        mdl.Option.objects.create(
            question=question,
            option=enums.LikertOptions.STRONGLY_AGREE,
            grade=10,
        )
        assert mdl.Option.objects.count() >= 1

    def test_update_option_successfully(self, option, question):
        assert not option.question == question
        option.question = question
        option.save()
        updated_option = mdl.Option.objects.get(pk=option.id)
        assert updated_option.question == question

    def test_delete_option_successfully(self, option):
        before_count = mdl.Option.objects.count()
        assert before_count >= 1
        option.delete()
        assert mdl.Option.objects.count() < before_count


@pytest.mark.unit
@pytest.mark.django_db
class TestQuestionnaireGroupModel:
    def test_create_questionnaire_group_successfully(self, profile):
        mdl.QuestionnaireGroup.objects.create(attendee=profile)
        assert mdl.QuestionnaireGroup.objects.count() >= 1

    def test_update_questionnaire_group_successfully(
        self, questionnaire_group, profile
    ):
        assert not questionnaire_group.attendee == profile
        questionnaire_group.attendee = profile
        questionnaire_group.save()
        updated_questionnaire_group = mdl.QuestionnaireGroup.objects.get(
            pk=questionnaire_group.id
        )
        assert updated_questionnaire_group.attendee == profile

    def test_delete_questionnaire_group_successfully(self, questionnaire_group):
        before_count = mdl.QuestionnaireGroup.objects.count()
        assert before_count >= 1
        questionnaire_group.delete()
        assert mdl.QuestionnaireGroup.objects.count() < before_count

    def test_questionnaire_group_change_history_created_successfully(
        self, questionnaire_group
    ):
        questionnaire_group.is_active = False
        questionnaire_group.save()

        history = questionnaire_group.history.all()
        assert len(history) == 2
