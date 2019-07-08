import os
from distutils.util import strtobool

from dotenv import load_dotenv
load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ.get('DB_NAME'),
    }
}



INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = strtobool(os.environ.get('DEBUG'))

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'
