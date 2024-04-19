from random import randint, uniform

from django.core.management.base import BaseCommand
from homeworkapp2.models import Product


class Command(BaseCommand):
    help = 'Generate product'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Количество продуктов для создания')

    def handle(self, *args, **kwargs):
        products = []
        count = kwargs.get('count')
        for i in range(1, count+1):
            products.append(Product(
                name = f'продукт {i}',
                description =  'описание для продукта',
                price = uniform(0.01, 999999.99),
                count = randint(1, 100),
            ))
        Product.objects.bulk_create(products)