from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home/index.html')

def hello(request):
    return render(request, 'home/hello.html')

def uppercase(request, name):
    name = name.upper()
    context = {
        "name": name
    }
    return render(request, 'home/name.html', context)

def users(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, 'home/users.html', context)