from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.softskills.api.v1 import views

router = DefaultRouter()

router.register(r"softskills", views.SoftskillViewSet)
router.register(r"questions", views.QuestionViewSet)
router.register(r"options", views.OptionViewSet)
router.register(r"questionnaires", views.QuestionnaireViewSet)
router.register(r"answers", views.AnswerViewSet)
router.register(r"softskill-trainings", views.SoftskillTrainingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "likert-options/",
        views.LikertOptionAPIView.as_view(),
        name="likert_options",
    ),
    path(
        "my-softskill-questionnaires/",
        views.MySoftskillQuestionnaireAPIView.as_view(),
        name="my_softskill_questionnaires",
    ),
    path(
        "<slug:slug>/random-questions/",
        views.RandomQuestionAPIView.as_view(),
        name="random_questions",
    ),
    path(
        "<slug:slug>/my-softskill-trainings/",
        views.MySoftskillTrainingAPIView.as_view(),
        name="my_softskill_trainings",
    ),
]
