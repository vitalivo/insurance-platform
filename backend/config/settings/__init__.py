from decouple import config as env_config

# Определяем какие настройки использовать
ENVIRONMENT = env_config('ENVIRONMENT', default='development')

if ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'testing':
    from .testing import *
else:
    from .development import *