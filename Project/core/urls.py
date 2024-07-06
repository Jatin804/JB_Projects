from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('log_in', views.log_in, name='log_in'),  
    path('sign_up', views.sign_up, name='sign_up'),
    path('log_out', views.log_out, name='log_out'),    
    path('services',views.services, name='services'),
    path('about', views.about, name='about'),
]