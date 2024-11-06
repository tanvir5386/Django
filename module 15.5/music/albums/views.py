from django.shortcuts import render, redirect
from . import forms, models

def edit_album(request, id):
    profile_id = models.AlbumEntry.objects.get(pk=id)
    profile = forms.AlbumForm(instance = profile_id)
    
    if request.method == 'POST':
        profile = forms.AlbumForm(request.POST, instance = profile_id)
        if profile.is_valid():
            profile.save()
            return redirect('homepage')
    return render(request,'edit_musician.html',{'id':profile})
