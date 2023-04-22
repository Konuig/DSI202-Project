from django.urls import path,include ,re_path
from .views import *

urlpatterns = [
    path('',Home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('badminton/<int:badminton_id>', Badminton , name="badminton"),
    path('about', About, name='about'),
    path('badmintons',Badmintons,name='badmintons'),
    path('register',register, name='register'),
    re_path(r'cart/add/(?P<badminton_id>[\w-]+)/$', add_to_cart,name="add_to_cart"),
    re_path(r'cart/list/$',cart_list,name="cart_list"),
]
