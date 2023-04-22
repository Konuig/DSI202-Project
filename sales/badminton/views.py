from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect, HttpRequest
from datetime import datetime
from .forms import RegisterForm
from django.contrib.auth import login
from django.urls import reverse
from .models import *


# Create your views here.

def Home(request) :
    return render(request, 'home.html')

def About(request) :
    return render(request, 'about.html')

def Badminton(request, badminton_id) :
    one_product = None
    try :
        one_product = Product.objects.get(id = badminton_id)
    except :
        print("ไม่พบสินค้า")
    context = {'product' : one_product}
    return render(request,'badminton.html',context)

def Badmintons(request) :
    all_products = Product.objects.all().order_by('-instock')
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

def add_to_cart(request, badminton_id):
    product = get_object_or_404(Product,id = badminton_id)
    cart_items = request.session.get('cart_items') or []

    #update existing items
    duplicated = False
    for c in cart_items :
        if c.get('id') == product.id :
            c['qty'] = int(c.get('qty') or '1' )+ 1
            duplicated = True

    #new insert
    if not duplicated :
        cart_items.append({'id':  product.id,
                          'name' : product.title ,
                          'qty' : 1, 
                          })
        
    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('cart_list',kwargs={}))

def cart_list(request) :
    cart_items = request.session.get('cart_items') or []
    total_qty = 0
    for c in cart_items :
        total_qty = total_qty + c.get('qty')

    request.session['cart_qty'] = total_qty
    return render(request,'product_cart.html', {'cart_items':cart_items})


