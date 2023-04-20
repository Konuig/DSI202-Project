from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect, HttpRequest
from datetime import datetime
from .forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse

all_products = [
    {'id' : 1 , 'title' : 'name1' , 'price' : 155500},
    {'id' : 2 , 'title' : 'name2' , 'price' : 400},
    {'id' : 3 , 'title' : 'name3' , 'price' : 200},]
# Create your views here.

def Home(request) :
    return render(request, 'home.html')

def About(request) :
    return render(request, 'about.html')

def Badminton(request, badminton_id) :
    one_product = None
    try :
        one_product = [f for f in all_products if f['id'] == badminton_id][0]        
    except IndexError :
        print('error')
    context = {'product' : one_product}
    return render(request,'badminton.html',context)

def Badmintons(request) :
    context = {'products' : all_products}
    return render(request,'badmintons.html', context)

def register(requst) :
    #POST
    if requst.method == "POST" :
        form = RegisterForm(requst.POST)
        if form.is_valid() :
            user = form.save()
            login(requst,user)
            return HttpResponseRedirect(reverse('home'))
    else :
        form = RegisterForm()

    #GET
    context = {'form' : form}
    return render(requst, 'register.html',context)