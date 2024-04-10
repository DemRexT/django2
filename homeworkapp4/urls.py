from django.urls import path
from .views import img_form
urlpatterns = [
    path('loud/', img_form, name="loud"),
]
