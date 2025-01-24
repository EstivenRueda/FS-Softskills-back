from apps.files import exceptions
from apps.files.constants import MAX_PATH_LENGTH, MAX_SIZE_MB


def validate_file_size(value):
    """
    Checks the size of the given file and raises an InvalidFileSizeError if the file size exceeds
    the maximum allowed size
    """
    max_size_mb = MAX_SIZE_MB
    if value.size > max_size_mb * 1024 * 1024:
        raise exceptions.InvalidFileSizeError(max_size_mb=MAX_SIZE_MB)


def validate_file_path_length(value):
    """
    Checks the length of the file path (name) and raises an InvalidFileNameError
    if it exceeds the maximum allowed length
    """
    max_path_length = MAX_PATH_LENGTH
    if len(value.name) > max_path_length:
        raise exceptions.InvalidFileNameError(max_path_length=max_path_length)
