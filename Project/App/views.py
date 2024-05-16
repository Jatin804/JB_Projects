from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def Services(request):
    return render(request, "Services.html")

def Courses(request):
    return render(request, "Courses.html")

def Contact(request):
    return render(request, "Contact.html")

def About(request):
    return render(request, "About.html")

