from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    """Модель страховых продуктов"""
    PRODUCT_TYPES = [
        ('osago', 'ОСАГО'),
        ('kasko', 'КАСКО'),
        ('ns', 'Несчастный случай'),
        ('klezh', 'Клещ'),
        ('mortgage', 'Ипотека'),
        ('ifl', 'Имущество физических лиц'),
    ]
    
    name = models.CharField(
        max_length=50, 
        choices=PRODUCT_TYPES,
        unique=True,
        verbose_name='Тип продукта'
    )
    display_name = models.CharField(
        max_length=100,
        verbose_name='Отображаемое название'
    )
    description = models.TextField(
        verbose_name='Описание продукта'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активен'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['display_name']
    
    def __str__(self):
        return self.display_name

class ProductField(models.Model):
    """Дополнительные поля для каждого продукта"""
    FIELD_TYPES = [
        ('text', 'Текстовое поле'),
        ('number', 'Числовое поле'),
        ('date', 'Дата'),
        ('choice', 'Выбор из списка'),
        ('decimal', 'Десятичное число'),
    ]
    
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='fields',
        verbose_name='Продукт'
    )
    field_name = models.CharField(
        max_length=50,
        verbose_name='Название поля'
    )
    field_type = models.CharField(
        max_length=20,
        choices=FIELD_TYPES,
        verbose_name='Тип поля'
    )
    is_required = models.BooleanField(
        default=False,
        verbose_name='Обязательное поле'
    )
    choices = models.JSONField(
        default=list,
        blank=True,
        verbose_name='Варианты выбора'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок отображения'
    )
    
    class Meta:
        verbose_name = 'Поле продукта'
        verbose_name_plural = 'Поля продуктов'
        ordering = ['product', 'order']
        unique_together = ['product', 'field_name']
    
    def __str__(self):
        return f"{self.product.display_name} - {self.field_name}"