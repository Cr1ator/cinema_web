from django.shortcuts import render
from home.models import About, Setting
from movies.models import Movie, MovieComment
from categories.models import Category
from django.apps import apps
# Create your views here.

def index(request):
    # print(apps.get_app_config('app_label').path)
    home = Setting.objects.latest('id')
    slide_movies = Movie.objects.all().order_by('-id')[:5]
    movies = Movie.objects.all().order_by('-id')[:8]
    one_random_movie = Movie.objects.all().order_by('?')
    one_random_genre = Movie.objects.all().order_by('?')[:1]
    categories = Category.objects.all().order_by('-id')
    most_popular_movie = Movie.objects.all().order_by('-genre')
    comments = MovieComment.objects.all().order_by('-id')
    context = {
        'home' : home,
        'movies' : movies,
        'slide_movies' : slide_movies,
        'one_random_movie' : one_random_movie,
        'one_random_genre' : one_random_genre,
        'categories' : categories,
        'most_popular_movie' : most_popular_movie,
        'comments' : comments,

    }
    return render(request, 'home/index.html', context)

def about(request):
    home = Setting.objects.latest('-id')
    about = About.objects.latest('id')
    context = {
        'home' : home,
        'about' : about, 
    }

    return render(request, 'home/about_us.html', context)

def avtor(request):
    home = Setting.objects.latest('-id')
    about = About.objects.latest('id')
    context = {
        'home' : home,
        'about' : about, 
    }

    return render(request, 'home/about_me.html', context)

def contakt(request):
    home = Setting.objects.latest('-id')
    about = About.objects.latest('id')
    context = {
        'home' : home,
        'about' : about, 
    }

    return render(request, 'home/contakt.html', context)