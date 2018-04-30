import datetime

from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Главная'
    popular_products = [
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-1.jpg',
            'image_href': '/products/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-2.jpg',
            'image_href': '/products/2/',
            'alt': 'продукт 2'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-3.jpg',
            'image_href': '/products/3/',
            'alt': 'продукт 3'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-4.jpg',
            'image_href': '/products/4/',
            'alt': 'продукт 4'
        }
    ]
    content = {'title': title,
               'popular_products': popular_products,
               'visit_date': datetime.datetime.now()}

    return render(request, 'index.html', content)


def contact(request):
    locations = [
        {'city': 'Москва',
         'phone': '555-55-55',
         'email': 'info@geekshop.ru',
         'address': 'В пределах МКАД'
         },
        {'city': 'Тюмень',
         'phone': '555-55-55',
         'email': 'info@geekshop.ru',
         'address': 'за МКАДом'
         },
        {'city': 'Рязань',
         'phone': '555-55-55',
         'email': 'info@geekshop.ru',
         'address': 'за МКАДом'
         }
    ]
    context = {'locations': locations,
               'visit_date': datetime.datetime.now()}

    return render(request, 'contact.html', context)
