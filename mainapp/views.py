import datetime
from django.shortcuts import render

from products.models import  Product
# Create your views here.


def index(request):
    title = 'Главная'

    popular_products = Product.get_featured_products()

    content = {'title': title,
               'featured_categories': ['Популярные', 'Новинки'],
               'featured_products': popular_products,
               'visit_date': datetime.datetime.now()}

    return render(request, 'index.html', content)


def contact(request):
    title = 'Контакты'

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
    context = {'title': title,
               'locations': locations,
               'visit_date': datetime.datetime.now()}

    return render(request, 'contact.html', context)
