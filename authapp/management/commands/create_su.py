from django.core.management.base import BaseCommand
from authapp.models import ShopUser


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **kwargs):
        ShopUser.objects.all().delete()
        # Создаем суперпользователя при помощи менеджера модели
        super_user = ShopUser.objects.create_superuser(username='admin',
                                                       email='test@test.com',
                                                       password='321456qwe')
