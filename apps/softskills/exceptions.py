from apps.core.exceptions import BaseDRFValidationError


class CurrentQuestionnaireNotFoundError(BaseDRFValidationError):
    default_detail = (
        "No se encontro un cuestionario completo para esta habilidad blanda."
    )
    default_code = "current_questionnaire_not_found"
