from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('books/', book, name='books'),
    path('books/create/', create_book, name='create_book'),
    path('books/all/', all_books, name='all_books'),
    path('games/', game, name='games'),
    path('games/create/', create_game, name='create_game'),
    path('games/all/', all_games, name='all_games'),
    path('movies/', movie, name='movies'),
    path('movies/create/', create_movie, name='create_movie'),
    path('movies/all/', all_movies, name='all_movies')
]