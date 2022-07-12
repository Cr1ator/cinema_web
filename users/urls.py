from django.urls import path 
from django.conf.urls.static import static
from users.views import register, user_login
from django.conf import settings

app_name = "users"
print("fsdfsd")

urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name='user_login'),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)