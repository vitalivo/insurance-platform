
from django.contrib import admin
from django.utils.html import format_html
from .models import ApplicationStatus, Application, ApplicationStatusHistory

@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_final', 'is_active']
    list_filter = ['is_final', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['order']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'full_name', 'product', 'status', 'created_at']
    list_filter = ['status', 'product', 'personal_data_consent', 'created_at']
    search_fields = ['application_number', 'full_name', 'email', 'phone']
    ordering = ['-created_at']
    readonly_fields = ['application_number', 'created_at', 'updated_at', 'user_ip', 'user_agent']
    
    fieldsets = (
        ('Информация о заявке', {
            'fields': ('application_number', 'product', 'status')
        }),
        ('Данные клиента', {
            'fields': ('full_name', 'phone', 'email', 'birth_date')
        }),
        ('Дополнительная информация', {
            'fields': ('additional_data', 'comment', 'admin_comment')
        }),
        ('Согласия и обработка', {
            'fields': ('personal_data_consent', 'processed_at')
        }),
        ('Техническая информация', {
            'fields': ('user_ip', 'user_agent', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ApplicationStatusHistory)
class ApplicationStatusHistoryAdmin(admin.ModelAdmin):
    list_display = ['application', 'old_status', 'new_status', 'changed_at']
    list_filter = ['old_status', 'new_status', 'changed_at']
    search_fields = ['application__application_number', 'application__full_name']
    ordering = ['-changed_at']
    readonly_fields = ['application', 'old_status', 'new_status', 'changed_at']
