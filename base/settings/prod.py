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

def read_env():
    env_path = ""
    for path, dirs, files in os.walk(os.getcwd()):
        for i in files:
            print(path)
            if i == '.env':
                setting_path = path
                break
    dotenv.read_dotenv(setting_path)
read_env()