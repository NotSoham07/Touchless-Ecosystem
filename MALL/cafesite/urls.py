"""cafesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cafe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('feedback/', views.feedback, name='feedback'),
    path('menu/', views.menu, name='menu'),
    path('joinus/', views.joinus, name = 'joinus'),
    path('tray/', views.tray, name = 'tray'),
    path('about/', views.about, name = 'about'),
    path('status/', views.status, name = 'status'),
    path('index/', views.index, name = 'index'),
    path('movies/', views.movies, name = 'movies'),
    path('seating/', views.seating, name = 'seating'),
    path('payment/', views.payment, name = 'payment'),
    path('tickets/', views.tickets, name = 'tickets'),
    path('front/', views.front, name = 'front'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
