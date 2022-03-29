from .dev import *

DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS -= [
    "debug_toolbar",
]

MIDDLEWARE -= [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

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
