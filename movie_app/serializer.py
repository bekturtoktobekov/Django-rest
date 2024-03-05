from rest_framework import serializers
from . import models
from rest_framework.exceptions import ValidationError

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = 'name count_movies'.split()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = 'text movie stars rating'.split()

class DirectorUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=2, max_length=20)

class MovieUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=2, max_length=20),
    description = serializers.CharField(min_length=2, max_length=100),
    duration = serializers.CharField(min_length=2, max_length=20)

    def validate_director_id(self, value):
        if models.Director.objects.filter(id=value).count() == 0:
            raise ValidationError(f'Category with id {value} does not exist')

class ReviewUpdateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=2, max_length=100),
    movie = MovieUpdateSerializer()
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_stars(self, value):
        if models.Reviews.objects.filter(id=value).count() == 0:
            raise ValidationError(f'Category with id {value} does not exist')
