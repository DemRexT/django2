from django.shortcuts import render
from django.db.models import Sum

from homeworkapp2.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('count'))
    context = {
        'title': 'общее количество товаров посчитаное в базе данных',
        'total': total,
    }
    return render(request, 'homework6/total_count.html', context)