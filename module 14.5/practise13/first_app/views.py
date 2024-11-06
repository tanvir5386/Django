from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def home(request):
    form = forms.PractiseForm()
    return render(request,'home.html',{'form':form})

def home1(request):
    model = models.MOdelPractise.objects.all()
    return render(request,'home1.html',{'model':model})