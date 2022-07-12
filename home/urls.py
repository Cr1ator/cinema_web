from django.urls import path 
from home.views import index, about, avtor,contakt
from django.conf.urls.static import static
from django.conf import settings


app_name = "home"

urlpatterns = [
    path('', index, name = "index"),
    path('about/', about, name = "about"),
    path('avtor/', avtor, name = "avtor"),
    path('contakt/', contakt, name = "contakt"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
