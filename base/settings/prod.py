import pathlib
from .common import *
import dotenv
import os
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
env_path = f"{str(Path(__file__).resolve().parent)}/.env"
dotenv.read_dotenv(env_path)