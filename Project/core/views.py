from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("Log_in")
    return render(request, "index.html")


def Log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is None:
            login(request, user)
            return render(request, 'index.html')
        else:
            login_error_message = "Invalid email or password"
            return render(request, 'login.html', {'form': form, 'login_error': login_error_message})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})



def Sign_up(request):
    return render(request, "sign_up.html")

def Log_out(request):
    pass


def Services(request):
    if request.user.is_anonymous:
        return redirect("Log_in")
    else:
        return render(request, "services.html")


def Review(request):
    if request.user.is_anonymous:
        return redirect("Log_in")
    return render(request, "review.html")


def About(request):
    if request.user.is_anonymous:
        return redirect("Log_in")
    else:
        return render(request, "about.html")
