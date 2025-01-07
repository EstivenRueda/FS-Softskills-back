from django.db import models


class SoftDeleteQuerySet(models.query.QuerySet):
    def delete(self):
        model_class = self.model

        if hasattr(model_class, "deleted"):
            n_objects = self.update(deleted=True)
        else:
            raise RuntimeError(f"Cannot soft-delete objects of type {model_class}")

        return n_objects, {model_class._meta.label: n_objects}

    def undelete(self):
        model_class = self.model

        if hasattr(model_class, "deleted"):
            n_objects = self.update(deleted=False)
        else:
            raise RuntimeError(f"Cannot un-delete objects of type {model_class}")

        return n_objects, {model_class._meta.label: n_objects}

    def deleted(self):
        return self.filter(deleted=True)

    def not_deleted(self):
        return self.filter(deleted=False)


class ActivableQuerySetMixin:
    def is_active(self):
        return self.filter(is_active=True)

    def is_inactive(self):
        return self.filter(is_active=False)


class BaseQuerySet(SoftDeleteQuerySet, ActivableQuerySetMixin):
    pass


class FilterDeletedObjectsManager(models.Manager):
    """
    A Django object manager (basis for executing queries) that automatically filters soft-deleted objects.
    """

    _queryset_class = SoftDeleteQuerySet

    def get_queryset(self):
        """Default queryset excludes the deleted records"""
        queryset = self._queryset_class(self.model, using=self._db)
        return self._filter_deleted_records(queryset)

    def _filter_deleted_records(self, queryset):
        model_class = self.model
        if hasattr(model_class, "deleted"):
            queryset = queryset.exclude(deleted=True)
        return queryset

    def deleted(self):
        queryset = self._queryset_class(self.model, using=self._db)

        model_class = self.model
        if hasattr(model_class, "deleted"):
            queryset = queryset.filter(deleted=True)
        return queryset

    def include_deleted(self):
        return self._queryset_class(self.model, using=self._db)


class BaseManager(FilterDeletedObjectsManager):
    _queryset_class = BaseQuerySet
