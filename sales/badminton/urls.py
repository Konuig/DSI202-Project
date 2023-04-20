from django.urls import path,include
from .views import *

urlpatterns = [
    path('',Home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('badminton/<int:badminton_id>', Badminton , name="badminton"),
    path('about', About, name='about'),
    path('badmintons',Badmintons,name='badmintons'),
    path('register',register, name='register'),
]
