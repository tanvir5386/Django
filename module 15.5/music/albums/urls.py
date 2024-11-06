from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path('albums/<int:id>',views.edit_album, name ='edit_album')
]
