
from django.contrib import admin
from .models import Product, ProductField

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['display_name', 'name', 'is_active', 'created_at']
    list_filter = ['is_active', 'name', 'created_at']
    search_fields = ['display_name', 'description']
    ordering = ['display_name']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'display_name', 'description')
        }),
        ('Настройки', {
            'fields': ('is_active',)
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ProductField)
class ProductFieldAdmin(admin.ModelAdmin):
    list_display = ['field_name', 'product', 'field_type', 'is_required', 'order']
    list_filter = ['product', 'field_type', 'is_required']
    search_fields = ['field_name']
    ordering = ['product', 'order']
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('product', 'field_name', 'field_type')
        }),
        ('Настройки поля', {
            'fields': ('is_required', 'order', 'choices')
        }),
    )
