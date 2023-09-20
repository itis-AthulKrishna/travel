from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . models import place
from . models import team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
