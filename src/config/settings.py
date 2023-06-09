import os

from distutils.util import strtobool
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv("DEBUG", "1")))

# SECURITY WARNING: don't run with all hosts allowed in production!
allowed_hosts = os.getenv("ALLOWED_HOSTS", "*")
ALLOWED_HOSTS = list(map(str.strip, allowed_hosts.split(",")))


# Applications
BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "apps.shared",
    "apps.customers",
]

THIRD_APPS = [
    "rest_framework",
    "knox",
    "simple_history",
    "drf_yasg",  # swagger
    "corsheaders",
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS


SWAGGER_SETTINGS = {
    "DOC_EXPANSION": "none",
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ("knox.auth.TokenAuthentication",),
}


MIDDLEWARE = [
    # CORS
    "corsheaders.middleware.CorsMiddleware",
    # Django default
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # simple history
    "simple_history.middleware.HistoryRequestMiddleware",
]


ROOT_URLCONF = "config.urls"


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


WSGI_APPLICATION = "config.wsgi.application"


#AUTH_USER_MODEL = "users.User"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5438"),
    }
}





if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es"
TIME_ZONE = "America/Bogota"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR, "static")
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CORS ALLOWED ORIGINS
# ALLOW ALL ORIGINS
CORS_ORIGIN_ALLOW_ALL = True
