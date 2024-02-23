# Generated by Django 5.0.2 on 2024-02-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='stars',
            field=models.PositiveIntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=1, verbose_name='Поставьте звезду'),
        ),
    ]