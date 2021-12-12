from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    creator = models.TextField()
    published_by = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    isbn = models.IntegerField(null=True)


class Game(models.Model):
    title = models.CharField(max_length=256)
    creator = models.TextField()
    release_date = models.DateField(blank=True, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    creator = models.TextField()
    release_date = models.DateField(blank=True, null=True)
