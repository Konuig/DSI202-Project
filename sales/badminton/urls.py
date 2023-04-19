from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name="home"),
    path('badminton/<int:badminton_id>', Badminton , name="badminton"),
    path('about', About, name='about')
]
