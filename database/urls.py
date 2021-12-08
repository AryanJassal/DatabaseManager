from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/book/', create_book, name='create_book')
]