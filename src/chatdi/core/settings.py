from os import getenv, makedirs, path
from pathlib import Path

from core.logging.conf import get_logging_config

# ======================================================
# Base settings for the Django project.
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('SECRET_KEY', 'secret')
DEBUG = int(getenv('DEBUG', 0))
ALLOWED_HOSTS = getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1, localhost').split(', ')
SITE_DOMAIN = getenv('SITE_DOMAIN', '')
SITE_BASE_URL = f'https://{SITE_DOMAIN}/'
PROXY_COUNT = int(p) if (p := getenv('PROXY_COUNT')) else None

# ======================================================
# CORS and CSRF configuration
# ======================================================
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = getenv('CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1:8000, http://localhost:8000').split(', ')

# ======================================================
# Installed apps and middleware
# ======================================================
DJANGO_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
THIRD_PARTY_APPS = []  # type: ignore[var-annotated]
LOCAL_APPS = [
	'apps.users',
]
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
	'core.middlewares.real_ip.RealIPMiddleware',
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ======================================================
# URL adnd WSGI
# ======================================================
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'


# ======================================================
# Database
# ======================================================
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': getenv('POSTGRES_DB', 'chatdi'),
		'USER': getenv('POSTGRES_USER', 'user'),
		'PASSWORD': getenv('POSTGRES_PASSWORD', 'password'),
		'HOST': getenv('SQL_HOST', 'localhost'),
		'PORT': getenv('SQL_PORT', '5432'),
		'ATOMIC_REQUESTS': True,
	}
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ======================================================
# Users
# ======================================================
# ======================================================
# Пользователи
# ======================================================
AUTH_USER_MODEL = 'users.User'

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


# ======================================================
# Локализация и часовой пояс
# ======================================================
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ======================================================
# REST API и Swagger
# ======================================================
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': [
		'core.api.permissions.HasExternalServiceAPIKey',
	]
}

SWAGGER_SETTINGS = {'SECURITY_DEFINITIONS': {'Api-Key': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}}}
SWAGGER_USE_COMPAT_RENDERERS = False


# ======================================================
# Setatic files (HTML, CSS, JavaScript, Images)
# ======================================================
STATIC_URL = 'static/'
STATIC_DIR = BASE_DIR / 'staticfiles'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [STATIC_DIR]


TEMPLATE_DIR = STATIC_DIR / 'templates'
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [TEMPLATE_DIR],
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


# ======================================================
# Redis, Celery, Caching
# ======================================================
REDIS_URL = getenv('REDIS_HOST', 'redis://127.0.0.1')
REDIS_PORT = int(getenv('REDIS_PORT', 6379))
REDIS_HOST = REDIS_URL.split('://')[1]

if not DEBUG:
	CACHES = {
		'default': {
			'BACKEND': 'django.core.cache.backends.redis.RedisCache',
			'LOCATION': f'{REDIS_URL}/1',
		}
	}

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_BROKER_URL = REDIS_URL
CELERY_BACKEND_URL = REDIS_URL
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_BACKEND = f'{REDIS_URL}/2'
CELERY_RESULT_EXPIRES = 60
CELERYD_MAX_TASKS_PER_CHILD = 100
CELERYD_PREFETCH_MULTIPLIER = 4

BROKER_URL = f'{REDIS_URL}/3'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}


# ======================================================
# Logging
# ======================================================
LOG_DIR = BASE_DIR / 'logs'

if not path.exists(LOG_DIR):
	makedirs(LOG_DIR)

LOGGING = get_logging_config(log_dir=LOG_DIR, debug=bool(DEBUG))
