from django.contrib import admin
from .models import ProductCategory, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ ProductImageInline, ]


# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)
