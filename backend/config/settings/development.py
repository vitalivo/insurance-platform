
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
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Дополнительные настройки для разработки
CORS_ALLOW_ALL_ORIGINS = True

# Логирование в консоль для разработки
LOGGING['handlers']['console']['level'] = 'DEBUG'

# SSL настройки для email (отключаем проверку сертификатов)
import ssl
EMAIL_SSL_CONTEXT = ssl.create_default_context()
EMAIL_SSL_CONTEXT.check_hostname = False
EMAIL_SSL_CONTEXT.verify_mode = ssl.CERT_NONE

# Переопределяем настройки из base.py для разработки
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
