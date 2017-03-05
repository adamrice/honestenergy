"""
Django settings for honestenergy project on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get('VENV') == 'production' else True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'compengine',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'honestenergy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'compengine/templates',
            'home/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'honestenergy.contrib.custom_context_processors.keychain', # NOTE(Debug): May have to import from honestenergy 2x up front
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'honestenergy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

if not DEBUG:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Update database configuration with $DATABASE_URL.
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)

    GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID')

    MAILCHIMP_USERNAME = os.environ.get('MAILCHIMP_USERNAME')
    MAILCHIMP_SECRET_KEY = os.environ.get('MAILCHIMP_SECRET_KEY')
    MAILCHIMP_LISTS = {
        'Leads': 'c3fa5fc97b',
    }

else:
    SECRET_KEY = 'XXXXXXXXXXXXXX'
    GOOGLE_ANALYTICS_ID = 'UA-XXXXX-X'
    MAILCHIMP_USERNAME = 'XXXXXXXXX'
    MAILCHIMP_SECRET_KEY = 'XXXXXXXXX'
    MAILCHIMP_LISTS = {
        'Leads': 'XXXXXXXXX',
    }

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Set up fixtures paths
FIXTURE_DIRS = [
    '/compengine/fixtures/',
    ]


# # Debug code to debug production server errors locally
# # As seen here: http://stackoverflow.com/questions/238081/how-do-you-log-server-errors-on-django-sites/6395837#6395837
# # DEBUG must be set to false
# DEBUG_LOGFILE = '/var/log/django/honestenergy.log'
# SECRET_KEY = 'XXXXXXXXXXXXXX'
# GOOGLE_ANALYTICS_ID = 'UA-XXXXX-X'
# MAILCHIMP_USERNAME = 'XXXXXXXXX'
# MAILCHIMP_SECRET_KEY = 'XXXXXXXXX'
# MAILCHIMP_LISTS = {
#     'Leads': 'XXXXXXXXX',
# }
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         # Include the default Django email handler for errors
#         # This is what you'd get without configuring logging at all.
#         'mail_admins': {
#             'class': 'django.utils.log.AdminEmailHandler',
#             'level': 'ERROR',
#              # But the emails are plain text by default - HTML is nicer
#             'include_html': True,
#         },
#         # Log to a text file that can be rotated by logrotate
#         'logfile': {
#             'class': 'logging.handlers.WatchedFileHandler',
#             'filename': DEBUG_LOGFILE
#         },
#     },
#     'loggers': {
#         # Again, default Django configuration to email unhandled exceptions
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         # Might as well log any errors anywhere else in Django
#         'django': {
#             'handlers': ['logfile'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         # Your own app - this assumes all your logger names start with "honestenergy."
#         'honestenergy': {
#             'handlers': ['logfile'],
#             'level': 'WARNING', # Or maybe INFO or DEBUG
#             'propagate': False
#         },
#     },
# }
