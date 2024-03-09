from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from . import serializer, models
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

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

@api_view(['POST'])
def authorization(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user:
        Token.objects.create(user=user).delete()
        token = Token.objects.create(user=user).data
        return Response(data={'key': token.key},
                        status=status.HTTP_200_OK)
    return Response(data={'error': "User not found"},
                    status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def register(request):
    username = request.data['username']
    password = request.data['password']
    if not username or not password:
        return Response(data={'error': "Username and password are required "},
                        status=status.HTTP_404_NOT_FOUND)
    if User.objects.filter(username=username).exists():
        return Response(data={'error': 'Username already exists.'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.create_user(username=username, password=password,
                                        status=status.HTTP_201_CREATED)
        if user:
            return Response(data={'Created successfully'})
        else:
            return Response(data={'error': 'Failed to create user.'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except:
        return Response(data={'error': 'Username already exists.'},
                        status=status.HTTP_400_BAD_REQUEST)


