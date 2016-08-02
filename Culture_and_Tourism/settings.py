"""
Django settings for Culture_and_Tourism project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
from django.core.urlresolvers import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda x: os.path.join(BASE_DIR, x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!cfp_47rmkd^ekg9fhd)e^80nlj$9^jve*_jp3!24q=j2$st))'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'easy_thumbnails',
    'redactor',
    'culture_tourism',
    'account',
    'social.apps.django_app.default',
    'taggit',
    'treebeard',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # translation
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'Culture_and_Tourism.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [location('templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Culture_and_Tourism.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('Uznation'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = True

gettext_noop = lambda s: s

LANGUAGES = (
    ('en', gettext_noop('English')),
    ('ru', gettext_noop('Russian')),
    ('uz', gettext_noop('Uzbek')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LOCALE_PATH = (
    location('locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = location('static')
STATICFILES_DIRS = (
    location('assets'),
)

LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = location('media/')


THUMBNAIL_ALIASES = {
    '': {
        'site_logo': {'size': (200, 200), 'crop': True},
        'logo_footer': {'size': (100, 29), 'crop': True},
        'slide': {'size': (389, 260), 'crop': True},
        'promo': {'size': (1280, 90), 'crop': True},

    }
}

REDACTOR_OPTIONS = {'lang': 'en', 'plugins': [
    'clips', 'textexpander', 'filemanager', 'fullscreen',
    'imagemanager', 'properties', 'source', 'table', 'video'
]
}
REDACTOR_UPLOAD = 'uploads/'
