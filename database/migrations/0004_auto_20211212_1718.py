# Generated by Django 3.2.9 on 2021-12-12 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20211211_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='published_on',
            new_name='release_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='creators',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='book',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genres',
        ),
        migrations.RemoveField(
            model_name='game',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='game',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genres',
        ),
        migrations.DeleteModel(
            name='Genres',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
