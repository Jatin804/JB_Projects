from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import IntegrityError
from .models import CustomUserCreationForm

#check user = Jatin12, jatin2004@gmail.com, hello@12345

# Create your views here.

def index(request):
    if request.user.is_anonymous:
        return redirect("log_in")
    return render(request, "index.html")


def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            try:

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')  # Redirect to a named URL instead of rendering template directly
                else:
                    login_error_message = "Invalid User or password"
                    return render(request, 'login.html', {'form': form, 'login_error': login_error_message})
                
            except Exception as err:
                return render(request, login.html, {'login_error': login_error_message})
        else:
            login_error_message = "Invalid email or password"
            return render(request, 'login.html', {'form': form, 'login_error': login_error_message})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})




def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')  # Use 'password1' for UserCreationForm
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/log_in')
                else:
                    return render(request, 'sign_up.html', {'form': form, 'error': 'Authentication failed'})
            except IntegrityError:
                return render(request, 'sign_up.html', {'form': form, 'error': 'User already exists'})
        else:
            return render(request, 'sign_up.html', {'form': form, 'error': 'Invalid form submission'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})



def log_out(request):
    logout(request)
    return redirect('/log_in')


def services(request):
    if request.user.is_anonymous:
        return redirect("/log_in")
    else:
        return render(request, "services.html")


def review(request):
    if request.user.is_anonymous:
        return redirect("/log_in")
    return render(request, "review.html")


def about(request):
    if request.user.is_anonymous:
        return redirect("/log_in")
    else:
        return render(request, "about.html")
