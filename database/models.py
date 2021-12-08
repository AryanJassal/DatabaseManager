from django.db import models
from django.conf import settings


class Genres(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = 'genres'
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.TextField()
    cover = models.ImageField(f'{settings.BASE_DIR}/static/icon_not_found.png')
    published_by = models.TextField(blank=True, null=True)
    published_on = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genres)
    isbn = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=256)
    creator = models.TextField()
    cover = models.ImageField(f'{settings.BASE_DIR}/static/icon_not_found.png')
    release_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=256)
    creators = models.TextField()
    cover = models.ImageField(f'{settings.BASE_DIR}/static/icon_not_found.png')
    release_date = models.DateField(blank=True, null=True)
    genres = models.ManyToManyField(Genres)
