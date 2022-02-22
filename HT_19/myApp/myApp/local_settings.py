# SECURITY WARNING: keep the secret key used in production secret!
from pathlib import Path
from .settings import *

SECRET_KEY = 'django-insecure-blo6x1_ss*23(ftn_!=0p820qfvdsg6!ov^j7#$c5cv66_7zsd'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
