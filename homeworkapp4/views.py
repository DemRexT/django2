import logging
from django.shortcuts import render
from .forms import ImgForm
from homeworkapp2.models import Imag


def img_form(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
             img = Imag(images = request.FILES)
             logging.info('Успешно')
    else:
        form = ImgForm()
    return render(request, 'app4/loading.html', {'form': form})