
from rest_framework import serializers
from .models import Application, ApplicationStatus
from products.serializers import ProductListSerializer

class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationStatus
        fields = ['id', 'name', 'description', 'color']

class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'product', 'full_name', 'phone', 'email', 
            'birth_date', 'additional_data', 'personal_data_consent', 'comment'
        ]
    
    def create(self, validated_data):
        # Автоматически устанавливаем статус "Новая"
        try:
            new_status = ApplicationStatus.objects.get(name="Новая")
            validated_data['status'] = new_status
        except ApplicationStatus.DoesNotExist:
            pass
        
        return super().create(validated_data)

class ApplicationSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    status = ApplicationStatusSerializer(read_only=True)
    
    class Meta:
        model = Application
        fields = [
            'id', 'application_number', 'product', 'status', 'full_name',
            'phone', 'email', 'birth_date', 'additional_data', 'comment',
            'personal_data_consent', 'created_at'
        ]
        read_only_fields = ['application_number', 'created_at']
