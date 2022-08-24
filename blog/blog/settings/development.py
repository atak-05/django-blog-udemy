from .base import *



ALLOWED_HOSTS = ['*']


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



