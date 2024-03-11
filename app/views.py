from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
            match request.POST['action']:
                case "registration":
                    username = request.POST['username']
                    password = request.POST['password']
                    password_confirm = request.POST['confirm_password']
                    if password==password_confirm:
                        try:
                            user = User.objects.create_user(username=username,
                                 password=password)
                            user_l = authenticate(request,username=username, password=password)
                            if user_l is not None:
                                login(request, user_l)
                                return redirect("index")
                        except Exception as e:
                            pass
                        
                case "login":
                    username = request.POST['username']
                    password = request.POST['password']
                    user = authenticate(request,username=username, password=password)
                    print(user)
                    if user is not None:
                        login(request, user)
                        return redirect("index")
                case _:
                    pass
        return render(request=request, template_name="avto.html", context=context)