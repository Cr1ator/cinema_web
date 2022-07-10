from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('categories.urls')),
    path('', include('home.urls')),
    path('', include('movies.urls')),
    path('', include('users.urls')),
    path ('accounts/', include('allauth.urls')),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
