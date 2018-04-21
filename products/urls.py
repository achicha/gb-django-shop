from django.urls import path
from products.views import products_view

urlpatterns = [
    path('<int:product_vendor_code>/', products_view, name='product_description'),
    path('', products_view, name='products'),
]
