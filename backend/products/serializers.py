
from rest_framework import serializers
from .models import Product, ProductField

class ProductFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductField
        fields = ['id', 'field_name', 'field_type', 'is_required', 'choices', 'order']

class ProductSerializer(serializers.ModelSerializer):
    fields = ProductFieldSerializer(many=True, read_only=True, source='productfield_set')
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'display_name', 'description', 'is_active', 'fields']

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'display_name', 'description']
        
# Добавьте в конец файла:
class ProductDetailSerializer(ProductSerializer):
    fields = serializers.SerializerMethodField()
    
    class Meta(ProductSerializer.Meta):
        fields = ProductSerializer.Meta.fields + ['fields']
    
    def get_fields(self, obj):
        from .models import ProductField
        fields = ProductField.objects.filter(product=obj)
        return [{'name': f.name, 'field_type': f.field_type, 'required': f.required} for f in fields]        
