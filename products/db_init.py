from .models import ProductCategory, Product, ProductImage


def load_category():
    new_categories = [('Все', 'все стулья'),
                      ('Дом', 'стулья для дома'),
                      ('Офис', 'стулья для офиса'),
                      ('Модерн', 'Новые стулья'),
                      ('Классика', 'Классические стулья')]

    for cat in new_categories:
        c = ProductCategory(name=cat[0], description=cat[1])
        c.save()


def load_products():
    new_products = [
        {'category_id': 1,
         'name': 'Супер стул1',
         'short_desc': 'Еще один стул',
         'description': 'Качество как всегда на высоте, надо брать!',
         'price': 1700,
         'quantity': 2,
         'image': 'product-21.jpg'
         },
        {'category_id': 3,
         'name': 'Супер стул2',
         'short_desc': 'Опять стул',
         'description': 'Качество отличное!',
         'price': 2700,
         'quantity': 3,
         'image': 'product-31.jpg'
         }
    ]

    for p in new_products:
        # add new product
        prod = Product(category_id=p['category_id'],
                       name=p['name'],
                       short_desc=p['short_desc'],
                       description=p['description'],
                       price=p['price'],
                       quantity=p['quantity'])
        prod.save()
        # add image to related product
        img = ProductImage(product_id=prod.id,
                           image=p['image'])
        img.save()
