"""
Django settings for finishing_school project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from datetime import timedelta
from os.path import join
from pathlib import Path

# from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-m9fv^w!(wgc89bdxjiv)3_kunzc!b#rbi_4u^%jt0l7&i!dclv"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "django.contrib.sites",
    # Third-party apps
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",  # Support Login with Google
    "dj_rest_auth.registration",
    "drf_standardized_errors",
    "drf_yasg",
    "corsheaders",
    "simple_history",
    "django_filters",
    "django_extensions",
    "whitenoise.runserver_nostatic",
    "apps.core",
    "apps.users",
    "apps.profiles",
    "apps.softskills",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "apps.users.middleware.MoveJWTCookieIntoTheBody",
    "apps.users.middleware.MoveJWTRefreshCookieIntoTheBody",
]

MIDDLEWARE += ("crum.CurrentRequestUserMiddleware",)

# django.contrib.sites
SITE_ID = 1


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "finishing_school"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}


CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://localhost:3001",
]
CORS_ALLOW_CREDENTIALS = True

SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "none",
    "SECURITY_DEFINITIONS": {
        "JWT [Bearer {JWT}]": {
            "name": "Authorization",
            "type": "apiKey",
            "in": "header",
        }
    },
    "USE_SESSION_AUTH": False,
}

FORCE_SCRIPT_NAME = "/"

ROOT_URLCONF = "finishing_school.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "finishing_school.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-co"

TIME_ZONE = "America/Bogota"

USE_I18N = True

USE_TZ = True

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Behaviors global settings
NAME_MAX_LENGTH = 60
DESCRIPTION_MAX_LENGTH = 255
OBSERVATIONS_MAX_LENGTH = 255

# Fixtures
FIXTURE_DIRS = (
    os.path.normpath(join(os.path.dirname(BASE_DIR), "production_fixtures")),
)

# Logging Configuration
LOGGER_PREFIX = "finishing_school_back"
FINISHING_SCHOOL_LOGLEVEL = os.environ.get("FINISHING_SCHOOL_LOGLEVEL", "DEBUG")
LOGGING_DIR = os.path.normpath(join(os.path.dirname(BASE_DIR), "logs"))
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "finishing_school_class_formatter": {
            "()": "finishing_school.logging.FinishingSchoolJsonFormatter",  # Reference to your custom formatter class
            "format": "%(levelname)s%(asctime)s%(name)s%(message)s%(module)s",
        },
    },
    "handlers": {
        "file": {
            "level": FINISHING_SCHOOL_LOGLEVEL,  # Adjust the desired logging level
            "class": "logging.FileHandler",
            "filename": os.path.join(
                LOGGING_DIR, "logs.log"
            ),  # File where logs will be stored
            "formatter": "finishing_school_class_formatter",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "debugger_file": {
            "level": FINISHING_SCHOOL_LOGLEVEL,
            "class": "logging.handlers.RotatingFileHandler",
            "filename": os.path.join(LOGGING_DIR, "logs_debugger.log"),
            "maxBytes": 10485760,  # 10 MB
            "backupCount": 5,  # Maintain 5 backup files
        },
    },
    "loggers": {
        f"{LOGGER_PREFIX}.core": {
            "handlers": ["file", "console"],
            "level": FINISHING_SCHOOL_LOGLEVEL,
            "propagate": True,
        },
    },
}

# Custom user app
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

DRF_STANDARDIZED_ERRORS = {
    "EXCEPTION_HANDLER_CLASS": "apps.core.exception_handler.FinishingSchoolExceptionHandler",
}

# djangorestframework-simplejwt
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

# dj-rest-auth
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_COOKIE": "_auth",  # Name of access token cookie
    "JWT_AUTH_REFRESH_COOKIE": "_refresh",  # Name of refresh token cookie
    "JWT_AUTH_HTTPONLY": False,  # Makes sure refresh token is sent
    "LOGIN_SERIALIZER": "apps.users.api.v1.serializers.LoginSerializer",
    "USER_DETAILS_SERIALIZER": "apps.users.api.v1.serializers.UserSerializer",
}


ACCOUNT_AUTHENTICATION_METHOD = "email"  # Use Email / Password authentication
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"  # Do not require email confirmation


# Google OAuth
GOOGLE_OAUTH_CLIENT_ID = os.environ.get("GOOGLE_OAUTH_CLIENT_ID", "")
GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET", "")
GOOGLE_OAUTH_CALLBACK_URL = os.environ.get("GOOGLE_OAUTH_CALLBACK_URL", "")

# django-allauth (social)
# Authenticate if local account with this email address already exists
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
# Connect local account and social account if local account with that email address already exists
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APPS": [
            {
                "client_id": GOOGLE_OAUTH_CLIENT_ID,
                "secret": GOOGLE_OAUTH_CLIENT_SECRET,
                "key": "",
            },
        ],
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    }
}
