# created by admin
# to redirect according to link 

from django.contrib import admin
from django.urls import path
from App import views


urlpatterns = [
    path('', views.index, name='Home'),
    path('Services',views.Services, name='Services'),
    path('Courses',views.Courses, name='Courses'),
    path('Contact', views.Contact, name='Contact'),
    path('About', views.About, name='About'),
        
]
