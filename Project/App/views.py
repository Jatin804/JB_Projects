Loginfrom django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def Services(request):
    return render(request, "Services.html")

def Sign_up(request):
    return render(request, "Signup.html")

def Login(request):
    return render(request, "Login.html")

def Review(request):
    return render(request, "Review.html")

def About(request):
    return render(request, "About.html")

