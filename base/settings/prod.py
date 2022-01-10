from .common import *

DEBUG = False

CSRF_TRUSTED_ORIGINS = ['https://*.honeycombpizza.link','http://172.17.0.1:8000']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'site3',
        'USER': 'sbsst',
        'PASSWORD': 'sbs123414',
        'HOST': '172.17.0.1',
        'PORT': '3306',
    }
}