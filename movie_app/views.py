from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializer, models
from  rest_framework import status

@api_view(['GET'])
def get_directors(request):
    directors = models.Director.objects.all()
    data = serializer.DirectorSerializer(directors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_certain_director(request, id):
    try:
        product_id = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    data = serializer.DirectorSerializer(product_id).data
    return Response(data=data)

@api_view(['GET'])
def get_movies(request):
    movies = models.Movie.objects.all()
    data = serializer.MovieSerializer(movies, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_certain_movie(request, id):
    try:
        product_id = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    data = serializer.MovieSerializer(product_id).data
    return Response(data=data)

@api_view(['GET'])
def get_reviews(request):
    reviews = models.Reviews.objects.all()
    data = serializer.ReviewSerializer(reviews, many=True).data
    return Response(data=data)

@api_view(['GET'])
def get_certain_review(request, id):
    try:
        product_id = models.Reviews.objects.get(id=id)
    except models.Reviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    data = serializer.ReviewSerializer(product_id).data
    return Response(data=data)
