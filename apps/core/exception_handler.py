from django.core.exceptions import NON_FIELD_ERRORS as DJ_NON_FIELD_ERRORS
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError as DjangoValidationError
from drf_standardized_errors.handler import ExceptionHandler
from rest_framework import exceptions
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import api_settings

DRF_NON_FIELD_ERRORS = api_settings.NON_FIELD_ERRORS_KEY


def convert_django_to_drf_validation_error(exc: DjangoValidationError):
    """
    Convert a Django ValidationError to a Django Rest Framework (DRF) ValidationError.

    This function translates a Django validation error, which may lead to an HTTP 500 status,
    into a DRF validation error, resulting in an HTTP 400 status. It reformats the error
    details to be consistent with DRF's error structure.

    Args:
        exc (DjangoValidationError): The Django ValidationError to be converted.

    Returns:
        DRFValidationError: The converted DRF ValidationError with the appropriate error details.

    Example:
        try:
            # Some Django validation code
            pass
        except DjangoValidationError as e:
            drf_validation_error = convert_django_to_drf_validation_error(e)
            raise drf_validation_error
    """
    if isinstance(exc, DjangoValidationError):
        try:
            data = exc.message_dict
        except AttributeError:
            data = exc.message
        if DJ_NON_FIELD_ERRORS in data:
            data[DRF_NON_FIELD_ERRORS] = data[DJ_NON_FIELD_ERRORS]
            del data[DJ_NON_FIELD_ERRORS]

        status_code = 400
        code = "fail"
        if hasattr(exc, "status_code"):
            status_code = exc.status_code
        if hasattr(exc, "code"):
            code = exc.code
        exc = DRFValidationError(detail=data, code=code)

        if status_code:
            exc.status_code = status_code
    return exc


class FinishingSchoolExceptionHandler(ExceptionHandler):
    def convert_known_exceptions(self, exc: Exception) -> Exception:
        if isinstance(exc, DjangoValidationError):
            return convert_django_to_drf_validation_error(exc)
        if isinstance(exc, ObjectDoesNotExist):
            return exceptions.NotFound(str(exc))
        return super().convert_known_exceptions(exc)
