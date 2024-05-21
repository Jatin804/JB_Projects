# created by admin
# to redirect according to link 

from django.contrib import admin
from django.urls import path
from App import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('Login', views.Login, name='Login'),  
    path('Sign_up', views.Sign_up, name='Sign_up'),
    # path('Loginout', views.Loginout, name='Loginout'),    
    path('Services',views.Services, name='Services'),
    path('About', views.About, name='About'),
    path('Review', views.Review, name='Review'),
       
]
