from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Log_in', views.Log_in, name='Log_in'),  
    path('Sign_up', views.Sign_up, name='Sign_up'),
    path('Log_out', views.Log_out, name='Log_out'),    
    path('Services',views.Services, name='Services'),
    path('Review', views.Review, name='Review'),
    path('About', views.About, name='About'),
       
]