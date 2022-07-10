from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from movies.models import Movie
from home.models import Setting
from categories.models import Category
from django.db.models import Q
from movies.forms import MovieCreateForm, MovieUpdateForm

# Create your views here.
def movie_detail(request, id):
    movie = Movie.objects.get(id = id)
    random_movies = Movie.objects.all().order_by('?')[:20]
    home = Setting.objects.latest('id')
    categories = Category.objects.all().order_by('?')[:5]
    context = {
        'movie' : movie,
        'random_movies' : random_movies,
        'home' : home,
        'categories' : categories,
    }
    return render(request, 'moviesingle.html', context)

def movie_search(request):
    movies = Movie.objects.all()
    print("---------")
    print(movies)
    qury_obj = request.GET.get('key')
    print("---------------------")
    print(qury_obj)
    home = Setting.objects.latest('id')
    if qury_obj:
        products = Movie.objects.filter(Q(title__icontains = qury_obj))
        print(products)
    context = {
        'home' : home, 
        'movies' : products,
        'products' : products,
    }
    return render(request, 'index.html', context)

def movie_create(request):
    form = MovieCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,

    }
    return render(request, 'moviegridfw.html', context)

def movie_update(request, id):
    movie = Movie.objects.get(id = id)
    form = MovieUpdateForm(request.POST or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movielist', movie.id)
    context = {
        'form' : form,
    }
    return render(request, 'moviegridfw.html', context)


def movie_delete(request, id):
    context ={}
 
    obj = get_object_or_404(Movie, id = id)
    if request.method =="POST":

        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "moviegridfw.html", context)