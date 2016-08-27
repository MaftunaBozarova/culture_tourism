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
import django.conf.locale

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
location = lambda x: os.path.join(BASE_DIR, x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!cfp_47rmkd^ekg9fhd)e^80nlj$9^jve*_jp3!24q=j2$st))'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

ALLOWED_HOSTS = ['*']

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
    'taggit',
    'treebeard',
    'ckeditor',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # translation
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'Culture_and_Tourism.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [location('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'Culture_and_Tourism.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('db.UzNation'),
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

EXTRA_LANG_INFO = {
    'uz': {
        'bidi': False,
        'code': 'uz',
        'name': 'Uzbek',
        'name_local': "O'zbekcha",  # unicode codepoints here
    },
}
django.conf.locale.LANG_INFO.update(EXTRA_LANG_INFO)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

LOCALE_PATHS = (
    location('locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = location('static')
STATICFILES_DIRS = (
    location('assets'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = location('media/')

THUMBNAIL_ALIASES = {
    '': {
        'logo_footer': {'size': (100, 29), 'crop': 'scale'},
        'slide': {'size': (701, 469), 'crop': 'scale'},
        'promo': {'size': (1280, 100), 'crop': 'scale'},
        'main_article': {'size': (400, 550), 'crop': 'scale'},
        'kechabugun': {'size': (506, 345), 'crop': 'scale'},
        'turism': {'size': (382, 502), 'crop': 'scale'},
        'news_index': {'size': (400, 550), 'crop': 'scale'},
        'big_text_content': {'size': (870, 500), 'crop': 'scale'},
        'related': {'size': (260, 185), 'crop': 'scale'},
        'sanat_small': {'size': (289, 217), 'crop': True},
        'rassom_big': {'size': (579, 216), 'crop': 'scale'},
        'kulo_big': {'size': (289, 432), 'crop': 'scale'},
        'zargar_big': {'size': (579, 217), 'crop': 'scale'},

    }
}

REDACTOR_OPTIONS = {'lang': 'en', 'plugins': [
    'clips', 'textexpander', 'filemanager', 'fullscreen',
    'imagemanager', 'properties', 'source', 'table', 'video'
]
                    }
REDACTOR_UPLOAD = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
