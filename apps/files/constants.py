from apps.files import enums

ALLOWED_IMAGES = (".jpg", ".jpeg", ".png", ".svg")
ALLOWED_FILES = ALLOWED_IMAGES + (
    ".pdf",
    ".txt",
    ".csv",
    ".doc",
    ".docx",
    "xls",
    ".xlsx",
    ".pptx",
)
MAX_SIZE_MB = 4
UNIQUE_PER_SOURCE_CATEGORIES = (enums.FileCategory.PHOTO, enums.FileCategory.LOGO)
MAX_PATH_LENGTH = 130
