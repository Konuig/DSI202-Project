from django.urls import path,include ,re_path
from .views import *

urlpatterns = [
    path('',Home, name="home"),
    path('', include("django.contrib.auth.urls")),
    path('badminton/<int:badminton_id>', Badminton , name="badminton"),
    path('about', About, name='about'),
    path('badmintons',Badmintons,name='badmintons'),
    path('serch',Serchfilter,name='serch'),
    path('accounts/register',register, name='register'),
    path('accounts/', include('allauth.urls')),
    re_path(r'cart/add/(?P<badminton_id>[\w-]+)/$', add_to_cart,name="add_to_cart"),
    re_path(r'cart/delete/(?P<badminton_id>[\w-]+)/$', cart_delete,name="cart_delete"),
    re_path(r'cart/list/$',cart_list,name="cart_list"),
    path('checkout',cart_checkout,name='checkout'),

]
