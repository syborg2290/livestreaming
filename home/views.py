from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


# MAIN PANELS

def home(request):
    # request.session['current_route'] = "home:home"
    return render(request, 'components/panels/home.html')


def rooms(request):
    # request.session['current_route'] = "home:rooms"
    return render(request, 'components/panels/rooms.html')


# SUB PANELS

def rooms_area(request, room_id):
    return render(request, 'components/panels/sub_panels/room_area.html')
