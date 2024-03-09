from django.contrib import admin
from django.urls import path, include
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.get_directors),
    path('api/v1/directors/<int:id>/', views.get_certain_director),
    path('api/v1/movies/', views.get_movies),
    path('api/v1/movies/<int:id>/', views.get_certain_movie),
    path('api/v1/reviews/', views.get_reviews),
    path('api/v1/reviews/<int:id>/', views.get_certain_review),
    path('api/v1/login/', views.authorization),
    path('api/v1/register/', views.register),
    path('api/v1/cbv/', include('class_based_views.urls'))

]
