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
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]
    
    def get_object(self):
        slug = self.kwargs.get('slug')
        
        # Проверяем кеш
        cache_key = f'product_detail_{slug}'
        cached_product = cache.get(cache_key)
        
        if cached_product:
            return cached_product
            
        # Если нет в кеше, получаем из БД
        product = super().get_object()
        
        # Кешируем на 30 минут
        cache.set(cache_key, product, 60 * 30)
        
        return product