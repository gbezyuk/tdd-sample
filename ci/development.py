from ci.settings import *
import os

DEBUG = True
TEMPLATE_DEBUG = True

#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = '/tmp/django-mail'

PROJECT_ROOT = '/d/sandbox/ci/'
SITE_ROOT = PROJECT_ROOT + 'ci/'
MEDIA_ROOT = SITE_ROOT + 'media/'
STATIC_ROOT = SITE_ROOT + 'static/'

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'cover')

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': PROJECT_ROOT + 'dev.db.sqlite3',
        }
}

ADMINS = (('Grigory Bezyuk', 'gbezyuk@gmail.com'))
MANAGERS = ADMINS

