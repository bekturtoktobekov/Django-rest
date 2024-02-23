from rest_framework import serializers
from . import models

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
