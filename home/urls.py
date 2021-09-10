from django.urls import path
from .views import (
    home,
    rooms,
    rooms_area
)

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
    path('rooms/', rooms, name='rooms'),
    path('rooms/<slug:room_id>/', rooms_area, name='room_area'),
]
