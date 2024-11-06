from django.shortcuts import render, redirect
from . import models, forms

def edit_musician(request, id):
    profile_id = models.MusicianDetails.objects.get(pk=id)
    profile = forms.MusicianForm(instance = profile_id)
    
    if request.method == 'POST':
        profile = forms.MusicianForm(request.POST, instance = profile_id)
        if profile.is_valid():
            profile.save()
            return redirect('homepage')
    return render(request,'edit_musician.html',{'id':profile})
