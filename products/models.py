from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='название категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    is_active = models.BooleanField(verbose_name='активная категория', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_active = models.BooleanField(verbose_name='существующий продукт', default=True)

    @staticmethod
    def get_featured_products(category_id=None, filter_out=None, max_items=3):
        """return total cost for user"""
        if not category_id:
            category_id = Product.objects.last().category_id
        # todo filter out duplicate products
        _items = Product.objects.filter(category_id=category_id)[:max_items]
        return _items

    def __str__(self):
        return "{} ({})".format(self.name, self.category.name)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images', blank=True)
