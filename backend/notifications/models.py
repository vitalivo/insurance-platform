
from django.db import models
from core.models import BaseModel
from applications.models import Application

class EmailTemplate(BaseModel):
    '''Шаблоны email уведомлений'''
    TEMPLATE_TYPES = [
        ('user_application', 'Уведомление пользователю о заявке'),
        ('admin_new_application', 'Уведомление админу о новой заявке'),
        ('status_change', 'Уведомление об изменении статуса'),
    ]
    
    name = models.CharField(
        max_length=100,
        verbose_name='Название шаблона'
    )
    template_type = models.CharField(
        max_length=30,
        choices=TEMPLATE_TYPES,
        verbose_name='Тип шаблона'
    )
    subject = models.CharField(
        max_length=200,
        verbose_name='Тема письма'
    )
    html_content = models.TextField(
        verbose_name='HTML содержимое'
    )
    text_content = models.TextField(
        blank=True,
        verbose_name='Текстовое содержимое'
    )
    
    class Meta:
        verbose_name = 'Шаблон email'
        verbose_name_plural = 'Шаблоны email'
        ordering = ['template_type', 'name']
    
    def __str__(self):
        return f'{self.name} ({self.get_template_type_display()})'

class EmailNotification(models.Model):
    '''Лог отправленных email уведомлений'''
    STATUS_CHOICES = [
        ('pending', 'Ожидает отправки'),
        ('sent', 'Отправлено'),
        ('failed', 'Ошибка отправки'),
        ('delivered', 'Доставлено'),
    ]
    
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='notifications',
        null=True,
        blank=True,
        verbose_name='Заявка'
    )
    template = models.ForeignKey(
        EmailTemplate,
        on_delete=models.CASCADE,
        verbose_name='Шаблон'
    )
    recipient_email = models.EmailField(
        verbose_name='Email получателя'
    )
    subject = models.CharField(
        max_length=200,
        verbose_name='Тема письма'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Время отправки'
    )
    error_message = models.TextField(
        blank=True,
        verbose_name='Сообщение об ошибке'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    
    class Meta:
        verbose_name = 'Email уведомление'
        verbose_name_plural = 'Email уведомления'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.recipient_email} - {self.subject}'
