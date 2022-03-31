from .dev import *

DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS.remove("debug_toolbar")
INSTALLED_APPS += []

MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
MIDDLEWARE += []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": env("DEV_DB_NAME"),
    #     "USER": env("DEV_DB_USER"),
    #     "PASSWORD": env("DEV_DB_PASSWORD"),
    #     "HOST": env("DEV_DB_HOST"),
    # },
}
