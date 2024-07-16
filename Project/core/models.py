from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.


# for reviews which will hold reviews 
class Users(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    review = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.username

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'check')

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    available_from = models.DateField()
    available_to = models.DateField()

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    hotel_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_form = models.DateField()
    date_to = models.DateField()


