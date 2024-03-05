from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializer, models
from rest_framework import status

@api_view(['GET', 'POST'])
def get_directors(request):
    if request.method == 'GET':
        directors = models.Director.objects.all()
        data = serializer.DirectorSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = serializer.DirectorUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        director = models.Director.objects.create(**request.data)
        return Response(data=serializer.DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def get_certain_director(request, id):
    try:
        product_id = models.Director.objects.get(id=id)
    except models.Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    if request.method == 'GET':
        data = serializer.DirectorSerializer(product_id).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'No such director'})
    elif request.method == 'PUT':
        product_id.name = request.data['name']
        return Response(data=serializer.DirectorSerializer(product_id).data,
                        status=status.HTTP_201_CREATED)




@api_view(['GET','POST'])
def get_movies(request):
    if request.method == 'GET':
        movies = models.Movie.objects.all()
        data = serializer.MovieSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = serializer.MovieSerializer(data=request.data)
        if serializers.is_valid():
            return Response(data={'errors': serializers.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        movie = models.Movie.objects.create(**request.data)
        return Response(data=serializer.MovieSerializer(movie))

@api_view(['GET', 'PUT', 'DELETE'])
def get_certain_movie(request, id):
    try:
        product_id = models.Movie.objects.get(id=id)
    except models.Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    if request.method == 'GET':
        data = serializer.MovieSerializer(product_id).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'No such movie'})
    elif request.method == 'PUT':
        product_id.name = request.data['name']
        product_id.description = request.data['description']
        product_id.rating = request.data['rating']
        product_id.duration = request.data['duration']
        return Response(data=serializer.MovieSerializer(product_id))






@api_view(['GET','POST'])
def get_reviews(request):
    if request.method == 'GET':
        reviews = models.Reviews.objects.all()
        data = serializer.ReviewSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializers = serializer.ReviewUpdateSerializer(data=request.data)
        if not serializers.is_valid():
            return Response(data={'errors': serializers.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        review = models.Reviews.objects.create(**request.data)
        return Response(data=serializer.ReviewSerializer(review))

@api_view(['GET', 'PUT', 'DELETE'])
def get_certain_review(request, id):
    try:
        product_id = models.Reviews.objects.get(id=id)
    except models.Reviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    if request.method == 'GET':
        data = serializer.ReviewSerializer(product_id).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product_id.delete()
        return Response(status=status.HTTP_204_NO_CONTENT,
                        data={'message': 'No such review'})
    elif request.method == 'PUT':
        product_id.title = request.data['title']
        product_id.description = request.data['description']
        product_id.duration = request.data['duration']
        product_id.director = request.data['director']
        return Response(data=serializer.ReviewSerializer(product_id))
