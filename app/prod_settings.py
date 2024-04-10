import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'fgbdrt4564(6od=fgd345ds=+d*a3+m1i2kdo!i@g-iqgs465hfo5)g+bw$4bh'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '185.177.219.252', 'xn--33-8kca3bm4bxd.xn--p1ai', 'xn--80aqbggmq6d.xn--p1ai']
CSRF_TRUSTED_ORIGINS = ['https://xn--80aqbggmq6d.xn--p1ai', 'https://xn--33-8kca3bm4bxd.xn--p1ai']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shariki24',
        'USER': 'shariki24',
        'PASSWORD': 'shariki24',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# STATICFILES_DIRS = [
#     BASE_DIR/'static'
# ]
