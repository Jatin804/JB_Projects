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


