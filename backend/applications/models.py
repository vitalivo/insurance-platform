
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from core.models import BaseModel
from products.models import Product

class ApplicationStatus(BaseModel):
    '''Статусы заявок'''
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название статуса'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    color = models.CharField(
        max_length=7,
        default='#6B7280',
        verbose_name='Цвет для UI',
        help_text='Цвет в формате HEX (#FF0000)'
    )
    is_final = models.BooleanField(
        default=False,
        verbose_name='Финальный статус',
        help_text='Статус, после которого заявка не может быть изменена'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения'
    )
    
    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name

class Application(BaseModel):
    '''Основная модель заявок'''
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='applications'
    )
    status = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        verbose_name='Статус',
        related_name='applications'
    )
    
    # Основные поля (обязательные для всех продуктов)
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    phone = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(10)],
        verbose_name='Телефон',
        help_text='Формат: +7XXXXXXXXXX'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    
    # Дополнительные данные в JSON (гибкость для разных продуктов)
    additional_data = models.JSONField(
        default=dict,
        blank=True,
        verbose_name='Дополнительные данные',
        help_text='Специфичные поля для каждого продукта'
    )
    
    # Согласие на обработку данных
    personal_data_consent = models.BooleanField(
        default=False,
        verbose_name='Согласие на обработку персональных данных'
    )
    
    # Комментарий пользователя
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий пользователя'
    )
    
    # Комментарий администратора
    admin_comment = models.TextField(
        blank=True,
        verbose_name='Комментарий администратора'
    )
    
    # Метаданные
    processed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата обработки'
    )
    
    # Техническая информация
    user_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name='IP адрес пользователя'
    )
    user_agent = models.TextField(
        blank=True,
        verbose_name='User Agent браузера'
    )
    
    # Номер заявки (автоматически генерируется)
    application_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        verbose_name='Номер заявки'
    )
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['product', 'created_at']),
            models.Index(fields=['application_number']),
        ]
    
    def __str__(self):
        return f'Заявка №{self.application_number} - {self.full_name}'
    
    def save(self, *args, **kwargs):
        # Автоматически генерируем номер заявки
        if not self.application_number:
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            self.application_number = f'APP-{timestamp}'
        super().save(*args, **kwargs)
    
    @property
    def is_processed(self):
        '''Проверяет, обработана ли заявка'''
        return self.status.is_final
    
    @property
    def days_since_created(self):
        '''Количество дней с момента создания'''
        from django.utils import timezone
        return (timezone.now() - self.created_at).days

class ApplicationStatusHistory(models.Model):
    '''История изменения статусов заявок'''
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='status_history',
        verbose_name='Заявка'
    )
    old_status = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        related_name='old_status_history',
        null=True,
        blank=True,
        verbose_name='Предыдущий статус'
    )
    new_status = models.ForeignKey(
        ApplicationStatus,
        on_delete=models.CASCADE,
        related_name='new_status_history',
        verbose_name='Новый статус'
    )
    comment = models.TextField(
        blank=True,
        verbose_name='Комментарий к изменению'
    )
    changed_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата изменения'
    )
    changed_by_ip = models.GenericIPAddressField(
        null=True,
        blank=True,
        verbose_name='IP адрес изменившего'
    )
    
    class Meta:
        verbose_name = 'История статуса'
        verbose_name_plural = 'История статусов'
        ordering = ['-changed_at']
    
    def __str__(self):
        return f'{self.application.application_number}: {self.old_status} → {self.new_status}'
