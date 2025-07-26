import os
from celery import Celery
from django.conf import settings

# Загружаем .env файл
from dotenv import load_dotenv
load_dotenv()


# Устанавливаем переменную окружения для Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем экземпляр Celery
app = Celery('insurance_platform')

# Загружаем конфигурацию из Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически находим задачи в приложениях
app.autodiscover_tasks()

# Конфигурация Celery
app.conf.update(
    broker_url='redis://localhost:6379',  # База 2 для Celery
    result_backend=os.getenv('CELERY_RESULT_BACKEND', 'redis://redis:6379/2'),
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Moscow',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 минут максимум
    task_soft_time_limit=25 * 60,  # 25 минут мягкий лимит
)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')