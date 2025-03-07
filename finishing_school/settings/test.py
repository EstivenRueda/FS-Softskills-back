from apps.core.utils import strtobool

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.getenv("DJANGO_DEBUG", "false"))

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "assets"))
STATICFILES_DIRS = [os.path.normpath(join(os.path.dirname(BASE_DIR), "static"))]
STATIC_URL = "/static/"

INTERNAL_IPS = [
    "127.0.0.1",
]
