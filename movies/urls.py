from django.urls import path 
from home.views import index,about
from movies.views import movie_detail, movie_search
from .models import Movie

urlpatterns = [
    path('', Movie, name = 'index'),
    path('movie-detail/<int:id>', movie_detail , name = 'movie_detail'), 
    path('movie-detail/<int:id>', movie_detail , name = 'movie_detail'), 
    path('search', movie_search, name="movie_search"),
]

