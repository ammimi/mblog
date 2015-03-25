"""
Django settings for mblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&m&dhoybccwb@q$%53fjrj8ecfvacnzakcl+=sz)w!9sr+75m&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'bootstrap_admin', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'article',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mblog.urls'

WSGI_APPLICATION = 'mblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, 'media'),
        )
''' 
TEMPLATE_DIRS = (
  os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
     )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
CKEDITOR_UPLOAD_PATH = "images/"

CKEDITOR_CONFIGS = {
    'mummy_default': {
           # 'toolbar': 'Full',
           'toolbar': (
                    ['div','Source','-','Save','NewPage','Preview','-','Templates'], 
                    ['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
                    ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
                    ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
                    ['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
                    ['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
                    ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
                    ['Link','Unlink','Anchor'], 
                    ['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
                    ['Styles','Format','Font','FontSize'], 
                    ['TextColor','BGColor'], 
                    ['Maximize','ShowBlocks','-','About', 'pbckcode'],
                     ),
           # 'height': 300,
           # 'width': 300,
               },
    }

