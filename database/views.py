from django import forms
from django.shortcuts import render

from .forms import *


def index(request):
    return render(request, 'page.html', {
        'book_form': NewBookForm()
    })


def create_book(request):
    pass