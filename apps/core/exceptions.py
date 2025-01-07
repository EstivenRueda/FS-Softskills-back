from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError as DRFValidationError


class BaseAPIException(APIException):
    """Use this class to create new specific API Exception classes.

    Example:
        class MyCustomException(BaseAPIException):
            status_code = status.HTTP_403_FORBIDDEN
            default_detail = _("You do not have permission to perform this action.")
            default_code = "permission_denied"
    """


class BaseDjangoValidationError(DjangoValidationError):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Invalid input."
    default_code = "invalid"

    def __init__(self, params=None):
        super().__init__(
            message=self.default_detail, code=self.default_code, params=params
        )


class BaseDRFValidationError(DRFValidationError):
    pass
