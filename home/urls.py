from django.urls import path

from .views import (
    home,
    rooms
)

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms, name='rooms'),
]
