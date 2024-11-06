from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name = 'homepage'),
    path('home1/', views.home1,name = 'homepage'),
]
