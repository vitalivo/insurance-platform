
from django.urls import path
from .views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<str:name>/', ProductDetailView.as_view(), name='product-detail'),
]
