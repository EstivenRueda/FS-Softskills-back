from django.db import models


class LikertOptions(models.TextChoices):
    STRONGLY_DISAGREE = "STRONGLY_DISAGREE", "Totalmente en desacuerdo"
    DISAGREE = "DISAGREE", "En desacuerdo"
    NEUTRAL = "NEUTRAL", "Ni de acuerdo / ni en desacuerdo"
    AGREE = "AGREE", "Algo de acuerdo"
    STRONGLY_AGREE = "STRONGLY_AGREE", "Totalmente de acuerdo"
