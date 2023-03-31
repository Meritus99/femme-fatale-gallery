"""
Django settings for coolsite project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import environ
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

""" All manipulations with 'env', for hiding the important data. """

# Here we read the .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    DEBUG=(bool, False)
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

#ALLOWED_HOSTS = env('HOST_1'), env('HOST_2'), env('LOCAL_HOST')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'captcha',
    'debug_toolbar',
    'women.apps.WomenConfig',
]

CAPTCHA_BACKGROUND_COLOR = '#f9d1ff'
CAPTCHA_IMAGE_SIZE = (150, 40)
CAPTCHA_LENGTH = 4

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'coolsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], #пишем путь для того чтобы переназначить стандарные шаблоны, взяв название файла base_site.html из папки venv, создадим файл с таким же названием в templates, но уже с кастомным содержимым, для того чтобы иметь возмож. настроить панель под себя. Это работает т.к джаного сначала ищет кастомные шаблоны для отображения страницы, а в случае их отсутствия, использует стандартные из venv. 
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

WSGI_APPLICATION = 'coolsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Для локальной машины

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "wenturum_django",
#         'USER': 'wenturum_django',
#         "PASSWORD": 'qNXuuZgR1_12',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en' # en-us

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

#LOGIN_REDIRECT_URL = '/'

INTERNAL_IPS = [
    "127.0.0.1",
]

# BASE_DIR хранит корневой каталог проекта 

""" Кэширование. Тут задается место, в котором будет содержаться сохраненный кэш. """
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'coolsite_cache'), 
    }
}

""" Для кэширования, в корневой папке проекта(coolsite) нужно создать папку с названием "coolsite_cache".
Можно кэшировать данные на уровне шаблонов(в файлах .html), с пом. API низкого уровня(в views.py или utils.py), и на уровне представлений(в urls.py).
Для кэширования на уровне представлений нужно в урлах прописать: 

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name='home'),
    ] 

"""