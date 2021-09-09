from django.shortcuts import render

# Create your views here.


def home(request):
    # request.session['current_route'] = "home:home"
    return render(request, 'components/panels/home.html')


def rooms(request):
    # request.session['current_route'] = "home:rooms"
    return render(request, 'components/panels/rooms.html')
