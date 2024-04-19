from django import forms
from homeworkapp2.models import Imag

class ImgForm(forms.Form):
    image = forms.ImageField()
