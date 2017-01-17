from WebApp.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'mysql',
        'PORT': 3306
    }
}
