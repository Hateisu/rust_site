from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
# Create your views here.

def index(request):
    context = {
        'rusts': RustVideo.objects.all(),
        'dota': DotaVideo.objects.all(),
        'user':request.user        }
    return render(request, 'index.html', context)

def rustvideobyid(request,id):
    context = {
        'video':RustVideo.objects.get(id=id)
        }
    return render(request, 'viderust1.html', context)

def dotavideobyid(request,id):
    context = {
        'video':DotaVideo.objects.get(id=id)
        }
    return render(request, 'viderust1.html', context)


def login_user(request):
    context = {}
    if request.user.is_authenticated:
        logout(request=request)
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("index")
        return render(request=request, template_name="avto.html", context=context)