import datetime

from django.shortcuts import render
from .models import ProductCategory, Product, ProductImage


def products_view(request, product_vendor_code=None):
    context = {}

    # upload product categories from DB
    product_categories = ProductCategory.objects.all()
    context.update({'product_categories': product_categories})

    # upload product details from DB using product_vendor_code

    # product_details = {
    #     1: {'product_params':
    #               {'product_name': 'Отличный стул',
    #                'picture': 'slider1.jpg',
    #                'red': 'горячее предложение',
    #                'price': 2585.9,
    #                'description': ['Расположитесь комфортно.',
    #                                'Отличное качество материалов позволит вам это.',
    #                                'Различные цвета',
    #                                'высочайший уровень эргономики и прочность.'],
    #                'diff_models': ['controll.jpg',
    #                                'controll1.jpg',
    #                                'controll2.jpg']}
    #           },
    #     2: {'product_params':
    #               {'product_name': 'Супер стул',
    #                'picture': 'product-11.jpg',
    #                'red': 'супер предложение',
    #                'price': 5000,
    #                'description': ['Описание обычного стула тут',
    #                                'Отличное качество материалов позволит вам это.',
    #                                'Различные цвета',
    #                                'высочайший уровень эргономики и прочность.'],
    #                'diff_models': ['controll.jpg',
    #                                'controll1.jpg',
    #                                'controll2.jpg']}
    #           },
    #     3: {'product_params':
    #          {'product_name': 'Супер стул',
    #           'picture': 'product-21.jpg',
    #           'red': 'супер предложение',
    #           'price': 7000,
    #           'description': ['Описание обычного стула тут',
    #                           'Отличное качество материалов позволит вам это.',
    #                           'Различные цвета',
    #                           'высочайший уровень эргономики и прочность.'],
    #           'diff_models': ['controll.jpg',
    #                           'controll1.jpg',
    #                           'controll2.jpg']}
    #      },
    #     4: {'product_params':
    #               {'product_name': 'Супер стул',
    #                'picture': 'product-31.jpg',
    #                'red': 'супер предложение',
    #                'price': 15000,
    #                'description': ['Описание обычного стула тут',
    #                                'Отличное качество материалов позволит вам это.',
    #                                'Различные цвета',
    #                                'высочайший уровень эргономики и прочность.'],
    #                'diff_models': ['controll.jpg',
    #                                'controll1.jpg',
    #                                'controll2.jpg']}
    #           }
    # }

    try:
        p = Product.objects.get(pk=product_vendor_code)
        imgs = ProductImage.objects.filter(product_id=p.id)
        ctx = {}
        ctx.update(p.__dict__)
        ctx.update({'images': imgs})
        context.update({'product_params': ctx})

    except Exception:
        p = Product.objects.get(pk=1)
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
