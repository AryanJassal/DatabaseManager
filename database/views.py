from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .forms import *
from .models import *


def index(request):
    return redirect('books')


def book(request):
    return render(request, 'book.html')


def create_book(request):
    if request.POST:
        data = request.POST
        attributes = {
            'title': data['title'],
            'creator': data['author'],
            'release_date': data['published_on'],
            'published_by': data['published_by'],
            'isbn': data['isbn']
        }
        
        create_new_entry(Book, attributes)

        return render(request, 'book.html', {
            'success': 'New book entry created successfully!'
        })
    else:
        return render(request, 'book.html', {
            'error': 'No data in POST header'
        })


def all_books(request):
    return return_all_entries(request, Book, 'book')


def game(request):
    return render(request, 'game.html')


def create_game(request):
    if request.POST:
        data = request.POST
        attributes = {
            'title': data['title'],
            'creator': data['creator'],
            'release_date': data['release_date']
        }

        create_new_entry(Game, attributes)

        return render(request, 'game.html', {
            'success': 'New game entry created successfully!'
        })
    else:
        return render(request, 'game.html', {
            'error': 'No data in POST header'
        })


def all_games(request):
    return return_all_entries(request, Game, 'game')


def movie(request):
    return render(request, 'movie.html')


def create_movie(request):
    if request.POST:
        data = request.POST
        attributes = {
            'title': data['title'],
            'creator': data['creator'],
            'release_date': data['release_date']
        }

        create_new_entry(Movie, attributes)

        return render(request, 'movie.html', {
            'success': 'New movie entry created successfully!'
        })
    else:
        return render(request, 'movie.html', {
            'error': 'No data in POST header'
        })


def all_movies(request):
    return return_all_entries(request, Movie, 'movie')


def create_new_entry(model, data):
    new_entry = model(**data)
    new_entry.save()
    return


def return_all_entries(request, model, name):
    objects = model.objects.all()
    paginator = Paginator(objects, 10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'all_entries.html', {
        'objects': page_obj,
        'category_name': name,
        'num_entries': model.objects.all().count()
    })