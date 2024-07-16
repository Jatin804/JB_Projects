from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import IntegrityError
from .models import CustomUserCreationForm, Hotel, Users, Booking
from datetime import datetime

#admin = Jatin, jatin@12345
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
        if request.method == 'POST':
            check_in = request.POST.get('check_in')
            check_out = request.POST.get('check_out')
            location = request.POST.get('location')

            if not check_in or not check_out or not location:
                return HttpResponse("Please provide all the required details.")

            try:
                check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
            except ValueError:
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.")

            # Filter hotels based on the location and availability dates
            available_hotels = Hotel.objects.filter(
                location=location,
                available_from__lte=check_in_date,
                available_to__gte=check_out_date
            )

            if available_hotels.exists():
                return render(request, "services.html", {'hotels': available_hotels})
            else:
                return HttpResponse("No hotels available for the selected dates and location.")
        else:
            # return HttpResponse("Invalid request method.")
            return render(request, "services.html")



def booking(request):
    if request.user.is_anonymous:
        return redirect("/log_in")
    else:
        if request.method == 'POST':
            hotel_name = request.POST.get('hotel_name')
            check_in = request.POST.get('date_from')
            check_out = request.POST.get('date_to')
            user_name = request.POST.get('user_name')  # Fetching from the form, not user object
            email = request.POST.get('email')  # Fetching from the form, not user object

            if not hotel_name or not check_in or not check_out or not user_name or not email:
                return HttpResponse("Please provide all the required details.")

            try:
                hotel = Hotel.objects.get(name=hotel_name)
                check_in_date = datetime.strptime(check_in, '%Y-%m-%d').date()
                check_out_date = datetime.strptime(check_out, '%Y-%m-%d').date()
            except Hotel.DoesNotExist:
                return HttpResponse("Hotel not found.")
            except ValueError:
                return HttpResponse("Invalid date format. Please use YYYY-MM-DD.")

            # Create a new Booking entry
            booking = Booking(
                name=user_name,
                hotel_name=hotel.name,
                location=hotel.location,
                date_from=check_in_date,
                date_to=check_out_date,
                email=email,
            )
            booking.save()

            return HttpResponse("Booking successful.")
        else:
            return render(request, "booking.html")


def about(request):
    if request.user.is_anonymous:
        return redirect("/log_in")
    else:
        return render(request, "about.html")
