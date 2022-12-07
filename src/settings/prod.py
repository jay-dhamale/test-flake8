from .base import *
DEBUG = True

ALLOWED_HOSTS = ["example.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev.sqlite3',
    }
}

X = "Path"