import re

from django.core.exceptions import ValidationError


def format_and_clean_str(text: str) -> str:
    """
    Format and title case a given text.

    This function takes a string as input, removes extra whitespaces between words,
    and then title cases the words. Title casing means that the first letter of
    each word is capitalized while the rest of the letters are in lowercase.

    Args:
        text (str): The input text to be formatted and title cased.

    Returns:
        str: The formatted and title cased text.
    """

    formatted_text = " ".join(text.split())
    return formatted_text


def sorted_alphanumeric(data: list) -> list:
    """
    Alphanumerically sorts a list.
    """

    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split("([0-9]+)", key)]

    return sorted(data, key=alphanum_key)


def strtobool(val):
    """Convert a string representation of truth to true (1) or false (0).

    True values are 'y', 'yes', 't', 'true', 'on', and '1'; false values
    are 'n', 'no', 'f', 'false', 'off', and '0'.  Raises ValueError if
    'val' is anything else.
    """
    val = val.lower()
    if val in ("y", "yes", "t", "true", "on", "1"):
        return 1
    if val in ("n", "no", "f", "false", "off", "0"):
        return 0
    raise ValueError(f"invalid truth value {val:!r}")


def map_history_type(history_type: str):
    type_mapping = {
        "+": "Creado",
        "~": "Cambiado",
        "-": "Removido",
    }
    return type_mapping.get(history_type, history_type)


def validate_password(password):
    """
    Validate the password to ensure it meets the following criteria:
    - At least 8 characters.
    - At least 1 capital letter.
    - At least 1 lower case letter.
    - At least 1 number.
    - At least 1 special character.
    """
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least 1 capital letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least 1 lower case letter.")
    if not re.search(r"[0-9]", password):
        raise ValidationError("Password must contain at least 1 number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValidationError("Password must contain at least 1 special character.")
