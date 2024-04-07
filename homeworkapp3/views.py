from django.shortcuts import render
from homeworkapp2.models import Order
from django.http import HttpResponse
from datetime import datetime, timedelta


def week(request):
    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)
    orders = Order.objects.filter(data__gte=seven_days_ago).order_by('-data')
    context = {'orders': orders}
    return render(request, 'app3/zakaz.html', context)


def month(request):
    today = datetime.now()
    seven_days_ago = today - timedelta(days=30)
    orders = Order.objects.filter(data__gte=seven_days_ago).order_by('-data')
    context = {'orders': orders}
    return render(request, 'app3/zakaz.html', context)


def year(request):
    today = datetime.now()
    seven_days_ago = today - timedelta(days=365)
    orders = Order.objects.filter(data__gte=seven_days_ago).order_by('-data')
    context = {'orders': orders}
    return render(request, 'app3/zakaz.html', context)