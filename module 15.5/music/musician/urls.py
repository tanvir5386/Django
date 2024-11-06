from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('edit/<int:id>', views.edit_musician, name ='edit_musician'),
]
