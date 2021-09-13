from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home'), name='home'),
    path("user/", include("user.urls", namespace="user"), name='user'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login/$', views.loginUser, name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
