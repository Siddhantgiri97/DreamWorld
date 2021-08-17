from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.


def cars_home(request):
    return render(request, 'cars_home.html')
