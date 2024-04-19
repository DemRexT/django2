from django.urls import path
from .views import total_in_db

urlpatterns = [
    path('db', total_in_db, name='db')
]
