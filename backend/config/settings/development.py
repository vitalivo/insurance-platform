
from .base import *

# Debug режим
DEBUG = True

# Добавляем debug toolbar для разработки
if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS += ['debug_toolbar']

if 'debug_toolbar.middleware.DebugToolbarMiddleware' not in MIDDLEWARE:
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + MIDDLEWARE

# Internal IPs для debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Email backend для разработки (выводит в консоль)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Дополнительные настройки для разработки
CORS_ALLOW_ALL_ORIGINS = True

# Логирование в консоль для разработки
LOGGING['handlers']['console']['level'] = 'DEBUG'
