from rest_framework import pagination

from apps.core.utils import strtobool


class UnpaginatableMixin:
    """
    Mixin to conditionally disable pagination in class-based views.

    This mixin class is used to disable pagination in class-based views under certain conditions.
    If the "get_all" parameter is provided in the query parameters of the GET request and has a value of 1 or "true",
    pagination will be disabled, and all results will be returned without being split into pages.
    Otherwise, standard pagination will be used.
    """

    def get_all(self, request):
        return strtobool(request.query_params.get("get_all", "false"))

    def paginate_queryset(self, queryset, request, view=None):
        """
        Overrides the pagination method to implement the pagination disabling functionality.
        """

        if self.get_all(request):
            return None

        return super().paginate_queryset(queryset, request, view=view)


class MainListPagination(pagination.PageNumberPagination):
    """
    Custom pagination class to control the pagination behavior for a principal list.

    This pagination class provides control over how a large list of items is divided into pages,
    allowing users to navigate through the list conveniently.

    Attributes:
        page_size (int): The number of items per page.
            Default is 10.

        page_query_param (str): The name of the query parameter that indicates the page number.
            Default is "page".

        page_size_query_param (str): The name of the query parameter that indicates the desired page size.
            Default is "page_size".

        max_page_size (int): The maximum allowed limit for the page size.
            Default is 25.
    """

    page_size = 10
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = 100
