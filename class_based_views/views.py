from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from movie_app.models import Reviews, Director, Movie
from movie_app.serializer import (ReviewSerializer,
                                  DirectorSerializer,
                                  MovieSerializer)
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class AuthorizationApiView(APIView):
    def post(self, request):
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


class RegistrationAPIView(APIView):
    def post(self, request):
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


class ReviewListApiView(ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['text']

class ReviewUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'id'



class DirectorListApiView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['name']

class DirectorUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'



class MovieListApiView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['title']

class MovieUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'
