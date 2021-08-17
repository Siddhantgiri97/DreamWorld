from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def bikes_home(request):
    return render(request, 'bikes_home.html')
