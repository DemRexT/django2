from django.contrib import admin
from .models import User, Order, Imag, Product


@admin.action(description="Поставить недействительную цену")
def prise(modeladmin, request, queryset):
    queryset.update(price=999999.99)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'price']
    actions = [prise]


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'data_reg']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'summa']


class ImgAdmin(admin.ModelAdmin):
    list_display = ['images']


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Imag, ImgAdmin)