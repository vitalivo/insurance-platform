
from django.db import models

class TimeStampedModel(models.Model):
    '''Абстрактная модель с временными метками'''
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    
    class Meta:
        abstract = True

class ActiveManager(models.Manager):
    '''Менеджер для активных записей'''
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BaseModel(TimeStampedModel):
    '''Базовая модель с активностью и временными метками'''
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    
    objects = models.Manager()
    active = ActiveManager()
    
    class Meta:
        abstract = True
