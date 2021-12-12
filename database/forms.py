from django import forms

from . import models


class NewBookForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-title'}))
    author = forms.CharField(label='Author', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-author'}))
    published_by = forms.CharField(label='Publisher', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-published_by'}))
    published_on = forms.DateField(label='Published', widget=forms.SelectDateWidget(attrs={'class': 'form-control', 'id': 'book-published_on'}))
    isbn = forms.IntegerField(label='ISBN13', widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'book-published_on'}))

    class Meta:
        model = models.Book
        fields = ['title', 'creator', 'published_by', 'release_date', 'isbn']
