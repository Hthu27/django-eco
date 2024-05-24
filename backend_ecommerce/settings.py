"""
Django settings for backend_ecommerce project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0=!u4xrlw*5!zx*0(y&t2lb^0%a@gii%4tk38-76xo!xv+gs1('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "cloudinary",
    "upload",
    'products',
    "rest_framework.authtoken",
    "djoser",
    "user",
    'orders'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
]
REST_FRAMEWORK = {
 'DEFAULT_AUTHENTICATION_CLASSES': (
 # Sử dụng JWT làm phương thức xác thực cho API
 'rest_framework_simplejwt.authentication.JWTAuthentication',
 ),
 'DEFAULT_PERMISSION_CLASSES': (
 # Định nghĩa các quyền truy cập cho API
 'rest_framework.permissions.IsAdminUser',
 'rest_framework.permissions.IsAuthenticated',
 'rest_framework.permissions.AllowAny',
 ),
}
from datetime import timedelta
SIMPLE_JWT = {
 # Thay đổi thời gian hết hạn của token
 'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
}
DJOSER = {
 # Disable tính năng gửi email kích hoạt tài khoản
 'SEND_ACTIVATION_EMAIL': False,
 'SERIALIZERS': {
 'user': 'user.serializers.UserAccountSerializer',
 'current_user': 'user.serializers.UserAccountSerializer',
 },
}
# Mặc định Django có User model rồi, 
# nên ta cần chỉ định lại User model trong trường hợp cần mở rộng User model
AUTH_USER_MODEL = 'user.UserAccount'

ROOT_URLCONF = 'backend_ecommerce.urls'

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

WSGI_APPLICATION = 'backend_ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import cloudinary.api
from decouple import config
cloudinary.config(
 cloud_name=config("CLOUDINARY_CLOUD_NAME"),
 api_key=config("CLOUDINARY_API_KEY"),
 api_secret=config("CLOUDINARY_API_SECRET"),
)