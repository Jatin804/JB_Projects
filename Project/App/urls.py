# created by admin
# to redirect according to link 

from django.contrib import admin
from django.urls import path
from App import views


urlpatterns = [
    path('', views.index, name="index") 
]
