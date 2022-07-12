from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve as mediaserve
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('categories.urls')),
    path('', include('home.urls')),
    path('', include('movies.urls')),
    path('', include('users.urls')),
    path ('accounts/', include('allauth.urls')),
]
