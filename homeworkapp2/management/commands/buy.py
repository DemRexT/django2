from django.core.management.base import BaseCommand
from homeworkapp2.models import Order, User, Product


class Command(BaseCommand):
    help = "Add User"


    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('pkprod', type=int, help='Product ID')


    def __str__(self):
        return f' name: {self.name}, email: {self.email}, number: {self.number}, adress: {self.adress}'


    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        pkprod = kwargs['pkprod']
        user = User.objects.get(id=pk)
        product = Product.objects.get(id=pkprod)
        order = Order(user=user)
        order.save()
        order.product.add(product)
        order.save()