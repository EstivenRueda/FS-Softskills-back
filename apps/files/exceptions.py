from apps.core.exceptions import BaseDjangoValidationError


class InvalidDocumentFormatError(BaseDjangoValidationError):
    default_detail = "Tipo de archivo no válido para un archivo de documento. Solo se permiten archivos %s."
    default_code = "Invalid_file_type_for_document_file"

    def __init__(self, allowed_files, params=None):
        self.default_detail = self.default_detail % allowed_files
        super().__init__(params=params)


class InvalidImageFormatError(BaseDjangoValidationError):
    default_detail = "Tipo de archivo no válido para un archivo de imagen. Solo se permiten archivos %s."
    default_code = "Invalid_file_type_for_image_file"

    def __init__(self, allowed_images, params=None):
        self.default_detail = self.default_detail % allowed_images
        super().__init__(params=params)


class InvalidFileSizeError(BaseDjangoValidationError):
    default_detail = "Tamaño de archivo no válido. Solo se permite un máximo de %d MB."
    default_code = "Invalid_file_size_for_a_file"

    def __init__(self, max_size_mb, params=None):
        self.default_detail = self.default_detail % max_size_mb
        super().__init__(params=params)


class UniqueImageCategoryError(BaseDjangoValidationError):
    default_detail = "Sólo se permite un %s por registro."
    default_code = "Unique_image_category_per_source"

    def __init__(self, categories, params=None):
        self.default_detail = self.default_detail % categories
        super().__init__(params=params)


class DuplicateFileNameError(BaseDjangoValidationError):
    default_detail = "Ya existe un archivo con el nombre '%s' para este registro."
    default_code = "Duplicate_file_name_per_source"

    def __init__(self, file_name, params=None):
        self.default_detail = self.default_detail % file_name
        super().__init__(params=params)


class InvalidFileNameError(BaseDjangoValidationError):
    default_detail = "El nombre del archivo no puede exceder %d caracteres."
    default_code = "Invalid_file_name"

    def __init__(self, max_path_length, params=None):
        self.default_detail = self.default_detail % max_path_length
        super().__init__(params=params)
