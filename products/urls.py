from django.urls import path
from products.views import products

app_name = 'products'

urlpatterns = [
    path('category/<int:category_pk>/', products, name='category'),
    path('<int:product_vendor_code>/', products, name='product_description'),
    path('', products, name='category'),
]
