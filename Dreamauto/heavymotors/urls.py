
from django.urls import path
from .import views

urlpatterns = [

    path('', views.heavymotors_home, name="heavymotors_home"),

]
