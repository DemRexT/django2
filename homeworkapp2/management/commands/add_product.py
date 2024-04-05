from django.core.management.base import BaseCommand
from homeworkapp2.models import Product


class Command(BaseCommand):
    help = "Add product"


    def __str__(self):
        return f' name: {self.name}, discription: {self.discription}, price: {self.price}, count: {self.count}'


    def handle(self, *args, **kwargs):
        product = Product(name = 'buts', description = 'Top buts!!', price = '19.99', count = '5')
        product.save()
