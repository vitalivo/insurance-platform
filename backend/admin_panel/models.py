
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

class Administrator(BaseModel):
    '''Модель администратора системы'''
    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Логин'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Телефон'
    )
    telegram_channel = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Telegram канал'
    )
    social_networks = models.JSONField(
        default=dict,
        blank=True,
        verbose_name='Социальные сети',
        help_text='JSON с ссылками на соцсети'
    )
    last_login = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Последний вход'
    )
    
    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'
        ordering = ['username']
    
    def __str__(self):
        return self.username

class AdminAction(models.Model):
    '''Логирование действий администратора'''
    ACTION_TYPES = [
        ('login', 'Вход в систему'),
        ('logout', 'Выход из системы'),
        ('status_change', 'Изменение статуса заявки'),
        ('data_export', 'Экспорт данных'),
        ('profile_update', 'Обновление профиля'),
    ]
    
    administrator = models.ForeignKey(
        Administrator,
        on_delete=models.CASCADE,
        related_name='actions',
        verbose_name='Администратор'
    )
    action_type = models.CharField(
        max_length=20,
        choices=ACTION_TYPES,
        verbose_name='Тип действия'
    )
    description = models.TextField(
        verbose_name='Описание действия'
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name='IP адрес'
    )
    user_agent = models.TextField(
        blank=True,
        verbose_name='User Agent'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время действия'
    )
    
    class Meta:
        verbose_name = 'Действие администратора'
        verbose_name_plural = 'Действия администраторов'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.administrator.username} - {self.get_action_type_display()}'
