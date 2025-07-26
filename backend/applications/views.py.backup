from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from django.core.cache import cache

from .models import Application
from .serializers import ApplicationCreateSerializer, ApplicationSerializer
from notifications.tasks import send_application_notification  # ✅ Только Celery задачи

class AdminApplicationListView(ListAPIView):
    """API для получения списка всех заявок (только для админов)"""
    queryset = Application.objects.all().order_by('-created_at')
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Фильтрация по статусу
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status__name=status_param)
        
        # Фильтрация по продукту
        product = self.request.query_params.get('product')
        if product:
            queryset = queryset.filter(product__id=product)
        
        return queryset

class AdminApplicationUpdateView(RetrieveUpdateAPIView):
    """API для обновления статуса заявки (только для админов)"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class ApplicationCreateView(generics.CreateAPIView):
    """Создание заявки - доступно всем"""
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer
    permission_classes = [AllowAny]

    def get_default_status(self):
        """Кешируем статус 'Новая' на 1 час"""
        cache_key = 'default_status'
        default_status = cache.get(cache_key)
        
        if not default_status:
            from .models import ApplicationStatus
            default_status = ApplicationStatus.objects.get(name='Новая')
            cache.set(cache_key, default_status, 60 * 60)
        
        return default_status

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save()
        
        # Подготавливаем данные для асинхронного уведомления
        notification_data = {
            'id': application.id,
            'product_name': application.product.display_name,
            'client_name': application.client_name,
            'client_email': application.client_email,
            'client_phone': application.client_phone,
            'created_at': application.created_at.strftime('%d.%m.%Y %H:%M'),
            'application_number': application.application_number,
            'client_ip': self.get_client_ip(request),
        }
        
        # ✅ Отправляем уведомление через Celery (асинхронно)
        send_application_notification.delay(notification_data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # ✅ Исправлено

    def get_client_ip(self, request):
        """Получаем IP адрес клиента"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class ApplicationDetailView(generics.RetrieveAPIView):
    """Просмотр заявки по номеру - доступно всем"""
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]
    lookup_field = 'application_number'