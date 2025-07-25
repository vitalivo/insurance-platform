
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Application
from .serializers import ApplicationCreateSerializer, ApplicationSerializer
from .utils import send_application_notification, send_sms_notification

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

class AdminApplicationListView(ListAPIView):
    """API для получения списка всех заявок (только для админов)"""
    queryset = Application.objects.all().order_by('-created_at')
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Фильтрация по статусу (если указан)
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status__name=status)
            
        # Фильтрация по продукту (если указан)
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
    queryset = Application.objects.all()
    serializer_class = ApplicationCreateSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Добавляем IP адрес и User Agent
        validated_data = serializer.validated_data
        validated_data['user_ip'] = self.get_client_ip(request)
        validated_data['user_agent'] = request.META.get('HTTP_USER_AGENT', '')
        
        application = serializer.save(**validated_data)
        self.perform_create_notifications(application)
        response_serializer = ApplicationSerializer(application)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    
    def perform_create_notifications(self, application):
    # Отправляем email уведомление
        try:
            send_application_notification(application)
            print(f"✅ Email уведомления отправлены для заявки #{application.application_number}")
        except Exception as e:
            print(f"❌ Ошибка отправки email: {e}")
        
    # Отправляем SMS уведомление
        try:
            send_sms_notification(application)
            print(f"✅ SMS уведомление отправлено для заявки #{application.application_number}")
        except Exception as e:
            print(f"❌ Ошибка отправки SMS: {e}")
        
        return application

class ApplicationDetailView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]
    lookup_field = 'application_number'
