import os
from pathlib import Path

import sib_api_v3_sdk
import environ
import dj_database_url


env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))  # Charge les variables d’environnement

# Utilisation des variables d’environnement
SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)

# Configuration de la base de données
DATABASES = {
    'default': dj_database_url.parse(env("DATABASE_URL"))
}
# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
AUTH_USER_MODEL = 'core.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "Sacko Services Admin",
    "site_header": "Sacko Services",
    "site_brand": "Sacko Services",
    # Logo to use for your site, must be present in static files, used for brand on top left
    #"site_logo": "books/img/logo.png",
}

# Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


# settings.py
SITE_NAME = "localhost"
DOMAIN = "localhost:4200"

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '/password-reset-confirm/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': True,
    'PASSWORD_RESET_TOKEN_TIMEOUT': 3600,

    'SERIALIZERS': {
        'user': 'core.serializers.CustomUserSerializer',
        'current_user': 'core.serializers.CustomUserSerializer',
        'password_reset': 'core.serializers.CustomPasswordResetSerializer',  # 👈 Ajout ici
    },
}




# CORS settings
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:4200",
    
# ]
CORS_ALLOW_ALL_ORIGINS = True

 # Adresse e-mail par défaut pour l'envoi

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")  # Remplace avec ton adresse e-mail
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # Remplace avec ton mot de passe
DEFAULT_FROM_EMAIL = "ismalsacko@yahoo.fr"





