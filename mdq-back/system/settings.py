from datetime import timedelta
from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == '1'
ALLOWED_HOSTS = [y for x in os.getenv('ALLOWED_HOSTS').split(',') if (y := x.strip())]

CORS_ALLOWED_ORIGINS = [y for x in os.getenv('CORS_ALLOWED_ORIGINS').split(',') if (y := x.strip())]
CSRF_TRUSTED_ORIGINS = [y for x in os.getenv('CSRF_TRUSTED_ORIGINS').split(',') if (y := x.strip())]

ROOT_URLCONF = 'system.urls'
WSGI_APPLICATION = 'system.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'turnstile',
    'django_bootstrap5',
    'mdq',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


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

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'django.contrib.auth.password_validation.{x}'}
    for x in [
        'UserAttributeSimilarityValidator',
        'MinimumLengthValidator',
        'CommonPasswordValidator',
        'NumericPasswordValidator'
    ]
]

AUTH_USER_MODEL = "mdq.MdqUser"

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Database
DATABASES = {'default': dj_database_url.config('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# Configuración de CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Vue desarrollo
    "http://localhost:3000",  # Ionic desarrollo
    "http://127.0.0.1:8080",
]

# Static files URL
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'assets'
MEDIA_URL = 'uploads/'
MEDIA_ROOT = BASE_DIR / 'uploads'

# Email
if os.getenv('EMAIL_AS_FILES', '0') == '1':
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
else:
    EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = os.getenv('EMAIL_HOST', '')
    EMAIL_PORT = os.getenv('EMAIL_PORT', '')
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', '')
    EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', '')
    EMAIL_TIMEOUT = os.getenv('EMAIL_TIMEOUT', '')
    EMAIL_SSL_KEYFILE = os.getenv('EMAIL_SSL_KEYFILE', '')
    EMAIL_SSL_CERTFILE = os.getenv('EMAIL_SSL_CERTFILE', '')

# Cloudflare's Turnstile
TURNSTILE_SITEKEY = os.getenv('TURNSTILE_SITEKEY')
TURNSTILE_SECRET = os.getenv('TURNSTILE_SECRET')

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=50),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
}
