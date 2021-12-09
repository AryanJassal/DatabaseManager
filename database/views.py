from django import forms
from django.shortcuts import render

from .forms import *
from .models import *


def index(request):
    return render(request, 'book.html', {
        'genres': Genres.objects.all()
    })


def create_book(request):
    pass