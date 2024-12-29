from rest_framework import pagination

from apps.core.utils import strtobool


class UnpaginatableMixin:
    def get_all(self, request):
        return strtobool(request.query_params.get("all", "false"))

    def paginate_queryset(self, queryset, request, view=None):
        """
        Overrides the pagination method to implement the pagination disabling functionality.
        """

        if self.get_all(request):
            return None

        return super().paginate_queryset(queryset, request, view=view)
