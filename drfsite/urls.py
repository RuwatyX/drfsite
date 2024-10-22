"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from dogs import views
from rest_framework import routers
import test1





urlpatterns = [
    path('admin/', admin.site.urls), # admin panel
    path("api/v1/dogs/", views.DogAPIList.as_view()),
    path("api/v1/dog/<int:pk>/", views.DogAPIUpdate.as_view()),
    path("api/v1/dogdelete/<int:pk>/", views.DogAPIDestroy.as_view()),
    path("api/v1/drf-auth/", include("rest_framework.urls")), # аутентификация по сессиям
    path("api/v1/auth/", include('djoser.urls')), # корень для действий с токенами
    re_path(r'^auth/', include('djoser.urls.authtoken')), 
    # маршрут для авторизации и выхода (auth/token/login | auth/token/logout)
    path("api/v2/", include('test1.urls')) # api/v2 -> test1.urls
]
