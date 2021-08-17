from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def whatsnew(request):
    return render(request, 'whatsnew.html')


def contact(request):
    return render(request, 'contact.html')
