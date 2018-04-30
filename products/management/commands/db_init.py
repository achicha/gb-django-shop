import os
import json

from django.core.management.base import BaseCommand
from products.models import ProductCategory, Product, ProductImage


JSON_PATH = 'products/json_products_data'


def load_json_data(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB with new data'

    def handle(self, *args, **kwargs):
        # load categories data
        categories = load_json_data('categories')
        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(name=category['name'],
                                           description=category['description'])
            new_category.save()

        # load products data
        products = load_json_data('products')
        Product.objects.all().delete()

        for p in products:
            # get category_id by name
            category_id = ProductCategory.objects.get(name=p['category']).id
            # add new product
            new_product = Product(category_id=category_id,
                                  name=p['name'],
                                  short_desc=p['short_desc'],
                                  description=p['description'],
                                  price=p['price'],
                                  quantity=p['quantity'])
            new_product.save()
            # add image to related product
            img = ProductImage(product_id=new_product.id,
                               image=p['image'])
            img.save()
