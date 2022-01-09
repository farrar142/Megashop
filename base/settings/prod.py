from .common import *

DEBUG = False

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