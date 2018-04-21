from django.shortcuts import render


def products_view(request, product_vendor_code=None):
    context = {}

    # upload product categories from DB
    product_categories = ['все', 'дом', 'офис', 'модерн', 'классика']
    context.update({'product_categories': product_categories})

    # upload product details from DB using product_vendor_code
    product_details = {
        1: {'product_params':
                  {'product_name': 'Отличный стул',
                   'picture': 'slider1.jpg',
                   'red': 'горячее предложение',
                   'price': 2585.9,
                   'description': ['Расположитесь комфортно.',
                                   'Отличное качество материалов позволит вам это.',
                                   'Различные цвета',
                                   'высочайший уровень эргономики и прочность.'],
                   'diff_models': ['controll.jpg',
                                   'controll1.jpg',
                                   'controll2.jpg']}
              },
        2: {'product_params':
                  {'product_name': 'Супер стул',
                   'picture': 'slider2.jpg',
                   'red': 'супер предложение',
                   'price': 15000,
                   'description': ['Описание обычного стула тут',
                                   'Отличное качество материалов позволит вам это.',
                                   'Различные цвета',
                                   'высочайший уровень эргономики и прочность.'],
                   'diff_models': ['controll.jpg',
                                   'controll1.jpg',
                                   'controll2.jpg']}
              }
    }

    try:
        context.update(product_details[product_vendor_code])
    except Exception:
        context.update(product_details[1])

    # upload related products from DB
    related_products = [
        {
            'image': 'product-11.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img'
        },
        {
            'image': 'product-21.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img'
        },
        {
            'image': 'product-31.jpg',
            'h4': 'Стул повышенного качества',
            'p': 'Не оторваться.',
            'alt': 'img'
        }
    ]
    context.update({'related_products': related_products})

    return render(request, 'products.html', context)
