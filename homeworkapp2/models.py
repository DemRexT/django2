from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    adress = models.CharField(max_length=100)
    data_reg = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2, default=999999.99)
    count = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    summa = models.DecimalField(max_digits = 100, decimal_places = 2, default = 0)
    data = models.DateTimeField(auto_now_add=True)


class Imag(models.Model):
    images = models.ImageField(upload_to='images/')
