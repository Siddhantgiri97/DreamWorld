
from django.urls import path
from .import views

urlpatterns = [

    path('', views.bikes_home, name="bikes_home"),

]
