"""intraviewer URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from core import views
from django.conf.urls.static import static
from mainapp import settings


urlpatterns = [
    
    path('', views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('history/', views.history, name='history'),
    path('interview/', views.interview, name='interview'),
    path('services/', views.services, name='services'),
    path('userindex/', views.userindex, name='userindex'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('privacy/', views.privacy, name='privacy'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

