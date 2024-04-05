from django.core.management.base import BaseCommand
from homeworkapp2.models import User


class Command(BaseCommand):
    help = "Add User"


    def __str__(self):
        return f' name: {self.name}, email: {self.email}, number: {self.number}, adress: {self.adress}'


    def handle(self, *args, **kwargs):
        user = User(name = 'Alex', email = 'alex123@mail.ru', number = '89117475327', adress = 'qwerty 1')
        user.save()
