"""
Django settings for trydjango18 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#root of project

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yqbj4k-xy8419luw9nu2go-#pnn+(2_236=xj_1e&#888o_it3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = (
    #django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #third party apps
    'crispy_forms',
    'storages',
    'gcm',  
    # 'registration',
    #my apps
    'project',
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
)
ROOT_URLCONF = 'sykopro.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'sykopro.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'syko',
#         'USER': 'postgres',
#         'PASSWORD': 'garg1995',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd85q7t8785jbol',               
        'USER': 'refyluzoiuuthg',
        'PASSWORD': '04ba2ab7deff190eb4865b883463a2376b0bf3eabc4554a60991fc280762a2b9',
        'HOST': 'ec2-54-225-88-191.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

    





# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'teamsykopro@gmail.com'
EMAIL_HOST_PASSWORD = 'sykokabadi'
DEFAULT_FROM_EMAIL = 'teamsykopro@gmail.com'
# DEFAULT_TO_EMAIL = ''



UNIQUE_KEY = "humteenomilkarekpapermillkholenge"
UNIQUE_KEY1 = "humteen"



# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/1.8/howto/static-files/


# STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_in_env")
# os.path.join(os.path.dirname(BASE_DIR), "/static_in_env")


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro"),
    #os.path.join(BASE_DIR, "static_in_env"),
    

 # 
)

# AWS_ACCESS_KEY_ID = "AKIAJBX2CXX7PHB4GYQA"
# AWS_SECRET_ACCESS_KEY = "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"
# AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-us-west-2-644902922622'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
# MEDIA_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
# ADMIN_MEDIA_PREFIX = MEDIA_URL + 'himaman/'


# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")


# crispy forms tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'



#django registration redux settings
# ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_AUTO_LOGIN = False
SITE_ID = 1
# LOGIN_REDIRECT_URL = '/'







