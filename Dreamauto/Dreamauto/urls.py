
from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('whatsnew/', views.whatsnew, name="whatsnew"),
    path('contact/', views.contact, name="contact"),
    path('cars/', include('cars.urls')),
    path('bikes/', include('bikes.urls')),
    path('heavymotors/', include('heavymotors.urls')),
]
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
