from django.urls import path
from .views import *
app_name='app1'
urlpatterns=[
    path('',home,name='home'),
    path('contact/',contact,name='contact'), 
    path('bootcamp/',bootcamp,name='bootcamp'),
]