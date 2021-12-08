from django import forms

from . import models


class NewBookForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'new-title'}))
    author = forms.CharField(label='Author', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'new-author'}))

    class Meta:
        model = models.Book
        fields = ['title', 'author', 'cover', 'published_by', 'published_on', 'genres', 'isbn']
