from django import forms

from . import models


class NewBookForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-title'}))
    author = forms.CharField(label='Author', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-author'}))
    published_by = forms.CharField(label='Publisher', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-published_by'}))
    published_on = forms.DateField(label='Published', widget=forms.SelectDateWidget(attrs={'class': 'form-control', 'id': 'book-published_on'}))
    # genres = forms.MultipleChoiceField(label='Genre(s)', choices=GENRES, widget=forms.ComboField(fields=GENRES))
    isbn = forms.IntegerField(label='ISBN13', widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'book-published_on'}))

    class Meta:
        model = models.Book
        fields = ['title', 'author', 'cover', 'published_by', 'published_on', 'genres', 'isbn']
