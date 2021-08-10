"""
Django settings for test_django project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gecgi8ltan#g3*4*@_5j8z$g0b)baym+)2is*six84bkdh$gv*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#打开可以设置自定义的404和500的报错HTML
# DEBUG = False
#
# ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  #如果将session存储在数据库中，需要在项INSTALLED_APPS中安装Session应用
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',
    'login',
    'captcha',  #验证码
    'ayla',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',#启用Session中间件，不启用删除掉该中间件即可
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#存储方式
#设置SESSION_ENGINE项指定Session数据存储的方式，可以存储在数据库、缓存、Redis等
#存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式
# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# 存储在缓存中：存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# 混合存储：优先从本机内存中存取，如果没有则从数据库中存取
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

ROOT_URLCONF = 'test_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'test_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False  #防止mysql数据库操作出问题

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = ''

CAPTCHA_IMAGESIZE = (8,45)   # 设置captcha图片大小

'''配置验证码的相关内容'''
CAPTCHA_LENGTH =4   #字符个数
CAPTCHA_TIMEOUT =1  #超时(minutes)*

# 输出格式：输入框验证码图片隐藏域•
# '%(image)s %(hidden_field)s %(text_field)s'
CAPTCHA_OUTPUT_FORMAT ='%(text_field)s %(image)s %(hidden_field)s'
CAPTCHA_NOISE_FUNCTIONS =(
    'captcha.helpers.noise_null',
    'captcha.helpers.noise_arcs',
    'captcha.helpers.noise_dots',
)
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'

#邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '411052590@qq.com'
EMAIL_HOST_PASSWORD = 'hlzxccpnunwabihi'
CONFIRM_DAYS = 1 #验证邮箱有效期