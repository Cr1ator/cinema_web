from django.urls import path 
from home.views import index, about, avtor,contakt



urlpatterns = [
    path('', index, name = "index"),
    path('about/', about, name = "about"),
    path('avtor/', avtor, name = "avtor"),
    path('contakt/', contakt, name = "contakt"),
]