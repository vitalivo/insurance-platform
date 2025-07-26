from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Product, ProductField
from .serializers import ProductSerializer, ProductDetailSerializer

# Кешируем список продуктов на 15 минут
@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductDetailView(generics.RetrieveAPIView):
    """Получение детальной информации о продукте"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    lookup_field = 'name'  # ✅ Используем 'name' вместо 'slug'
    permission_classes = [AllowAny]
    
    def get_object(self):
        """Кешируем детальную информацию о продукте"""
        name = self.kwargs.get('name')
        cache_key = f'product_detail_{name}'
        
        cached_product = cache.get(cache_key)
        if not cached_product:
            product = super().get_object()
            cache.set(cache_key, product, 60 * 15)  # 15 минут
            return product
        return cached_product