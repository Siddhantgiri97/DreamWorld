from django.shortcuts import render


def heavymotors_home(request):
    return render(request, 'heavymotors_home.html')
