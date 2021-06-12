import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Local(Common):
    DEBUG = True

    # CORS configuration for development needs
    
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:8080",
    ]

    CORS_ALLOW_METHODS = [
        'GET',
        'OPTIONS',
    ]

    # Testing
    INSTALLED_APPS = Common.INSTALLED_APPS
    INSTALLED_APPS += ('django_nose',)
    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        BASE_DIR,
        '-s',
        '--nologcapture',
        '--with-coverage',
        '--with-progressive',
        '--cover-package=datality_admin',
        '--verbosity=2'
    ]

    # Change to True for purpose of running tests only!
    # This overwrites common setting, look there for details
    MANAGE_EXTERNAL_DATABASES = True

    # Mail
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = 1025
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
