from typing import List, Tuple

from apps.core import utils


def resolve_model_change_to_str_values(
    original_obj: "Model", change: "ModelChange"
) -> Tuple[str, str]:
    """
    Retrieve string representations of old and new values based on a Django model change.

    Args:
        original_obj (django.db.models.Model): Django model instance.
        change (simple_history.models.ModelChange): The change object containing information about the modification.

    """
    old_value = change.old
    new_value = change.new
    # Obtain the model class and field information
    model_class = original_obj._meta.model
    field = getattr(model_class, change.field)
    # Check if the field is a ForeignKey to another model
    related_model = field.field.related_model
    if related_model is not None:
        # Retrieve string representations of the old and new ForeignKey values
        old_value = str(related_model.objects.filter(pk=old_value).first())
        new_value = str(related_model.objects.filter(pk=new_value).first())
    return old_value, new_value


def generate_change_list(
    historical_obj: "HistoricalModel", original_obj: "Model"
) -> List:
    """
    Compares two instances of a historical object and its original version, generating a list of changes between them.

    Args:
    - historical_obj (HistoricalObject): The current version of the historical object.
    - original_obj (django.db.models.Model): Django model instance.
    """
    changes = []
    # Check if there is a previous record to compare against
    if historical_obj.prev_record:
        # Calculate the difference between the current and previous records
        delta = historical_obj.diff_against(historical_obj.prev_record)
        for change in delta.changes:
            # Retrieve string representations of the old and new values
            old_value_str, new_value_str = resolve_model_change_to_str_values(
                original_obj, change
            )
            change_data = {
                "field": change.field,
                "from": old_value_str,
                "to": new_value_str,
            }
            changes.append(change_data)
    return changes


def get_object_history_changes(obj: "Model") -> List:
    """
    Retrieves the history of changes for a given object by iterating through its historical records.

    Args:
    - obj: The object for which the history is to be retrieved.

    """
    history_list = []

    # Iterate through historical records, ordered by date in descending order
    for historical_obj in obj.history.all().order_by("-history_date"):
        history_data = {
            "object_id": historical_obj.id,
            "history_id": historical_obj.history_id,
            "history_date": historical_obj.history_date.strftime("%Y-%m-%d"),
            "history_user": (
                historical_obj.history_user.email
                if historical_obj.history_user
                else None
            ),
            "history_type": utils.map_history_type(historical_obj.history_type),
            "changes": generate_change_list(historical_obj, obj),
        }
        history_list.append(history_data)
    return history_list
