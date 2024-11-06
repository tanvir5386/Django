from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete/<int:id>', views.delete_temp, name ='delete_temp'),
    path('musician/', include('musician.urls')),
    path('albums/', include('albums.urls')),
     path('', views.show_musicians, name = 'homepage')
]
