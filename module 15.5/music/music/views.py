from django.shortcuts import render, redirect
from albums.models import  AlbumEntry
# Create your views here.
# def home(request):
    # return render(request,'home.html')


# Create your views here.
def show_musicians(request):
    musicians = AlbumEntry.objects.all()
    
    return render(request,'home.html',{'musicians':musicians})

def delete_temp(request, id):
    
    album = AlbumEntry.objects.get(pk =id)
    album.delete()
    return redirect('homepage')