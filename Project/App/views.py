from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.

def index(request):
    return render(request, "index.html")

def Login(request):
    return render(request, "Login.html")

def Sign_up(request):
    return render(request, "Sign_up.html")

def Services(request):
    return render(request, "Services.html")

def Review(request):
    return render(request, "Review.html")

def About(request):
    return render(request, "About.html")

