from django.shortcuts import render

# Create your views here.


def index_view(request):
    title = 'Главная'
    popular_products = [
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-1.jpg',
            'image_href': '/product/1/',
            'alt': 'продукт 1'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-2.jpg',
            'image_href': '/product/2/',
            'alt': 'продукт 2'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-3.jpg',
            'image_href': '/product/3/',
            'alt': 'продукт 3'
        },
        {
            'name': 'Стул повышенного качества',
            'desc': 'Не оторваться.',
            'image_src': 'product-4.jpg',
            'image_href': '/product/4/',
            'alt': 'продукт 4'
        }
    ]
    content = {'title': title, 'popular_products': popular_products}

    return render(request, 'index.html', content)


def contact_view(request):
    return render(request, 'contact.html', {})
