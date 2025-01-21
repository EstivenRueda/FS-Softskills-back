import os
from os.path import join

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

CORS_ALLOWED_ORIGINS += os.environ.get("CORS_ALLOWED_ORIGINS", "").split(" ")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = os.path.normpath(join(os.path.dirname(BASE_DIR), "assets"))
STATIC_URL = "/static/"
MEDIA_ROOT = os.getenv("MEDIA_ROOT")
