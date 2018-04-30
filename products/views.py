import datetime

from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import ProductCategory, Product, ProductImage


def products(request, product_vendor_code=None):
    context = {}

    # upload product categories from DB
    product_categories = ProductCategory.objects.all()
    context.update({'product_categories': product_categories})

    try:
        p = Product.objects.get(pk=product_vendor_code)
        imgs = ProductImage.objects.filter(product_id=p.id)
        ctx = {}
        ctx.update(p.__dict__)
        ctx.update({'images': imgs})
        context.update({'product_params': ctx})

    except ObjectDoesNotExist:
        p = Product.objects.last()
        imgs = ProductImage.objects.filter(product_id=p.id)
        ctx = {}
        ctx.update(p.__dict__)
        ctx.update({'images': imgs})
        context.update({'product_params': ctx})

    # upload related products from DB
    # todo get products from related category from DB
    related_products = [
        {
            'image': 'product-11.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img',
            'id': 2
        },
        {
            'image': 'product-21.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img',
            'id': 3
        },
        {
            'image': 'product-31.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img',
            'id': 4
        }
    ]
    context.update({'related_products': related_products,
                    'visit_date': datetime.datetime.now()})

    return render(request, 'products.html', context)
