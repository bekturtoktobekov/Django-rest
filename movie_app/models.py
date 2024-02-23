from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=20)

    @property
    def count_movies(self):
        return self.movies.count()

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title

    @property
    def count_avg_reviews(self):
        reviews = Reviews.objects.filter(movie=self)
        if reviews.exists():
            total_stars = sum(review.stars for review in reviews)
            return total_stars/len(reviews)
        else:
            return 0


class Reviews(models.Model):
    STARS = (
        (1, '1 звезда'),
        (2, '2 звезды'),
        (3, '3 звезды'),
        (4, '4 звезды'),
        (5, '5 звезд'),
    )
    text = models.TextField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(choices=STARS, verbose_name='Поставьте звезду', blank=False, default=1)

    def rating(self):
        return self.stars

    def __str__(self):
        return f'Review for: {self.movie.title}'