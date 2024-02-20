from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    text = models.TextField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'Review for: {self.movie.title}'