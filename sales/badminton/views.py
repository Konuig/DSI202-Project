from django.shortcuts import render , get_object_or_404 
from django.http import HttpResponse , HttpResponseRedirect, HttpRequest
from datetime import datetime
from .forms import RegisterForm , ProductTitleFilter
from django.contrib.auth import login
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def Home(request) :
    return render(request, 'home.html')

def Serchfilter(request) :
    title = request.GET.get('title')
    product = Product.objects.all()
    if title:
        product = product.filter(title__icontains=title)
    context = {'form_S' : ProductTitleFilter(),
               'product_S' : product}
    return render(request, 'serch.html', context)

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

@login_required
def add_to_cart(request, badminton_id):
    product = get_object_or_404(Product,id = badminton_id)
    cart_items = request.session.get('cart_items') or []

    try :
        #update existing items
        duplicated = False
        for c in cart_items :
            if c.get('id') == product.id :
                c['qty'] = int(c.get('qty') or '1' ) + 1
                c['total_price'] = str(float((c.get('special_price')) or c.get('price')) * float(c.get('qty')))
                duplicated = True

        #new insert
        if not duplicated :
            cart_items.append({'id':  product.id,
                            'name' : product.title ,
                            'qty' : 1, 
                            'price' : str(product.price),
                            'special_price' : str(product.special_price) or None , 
                            'total_price' : str(product.special_price) or str(product.price)
                            })
    except :
        pass
            
    request.session['cart_items'] = cart_items
    return HttpResponseRedirect(reverse('cart_list',kwargs={}))

@login_required
def cart_list(request) :

    cart_items = request.session.get('cart_items') or []
    total_qty = 0
    total_cart_price = 0
    for c in cart_items :
        total_qty = total_qty + c.get('qty')
        total_cart_price = total_cart_price + float(c.get('total_price'))

    request.session['cart_qty'] = total_qty
    request.session['cart_price'] = total_cart_price

    context = {'cart_items':cart_items}
    return render(request,'product_cart.html', context)


def cart_delete(request,badminton_id) :
    cart_items = request.session.get('cart_items') or []
    for i in range(len(cart_items)) :
        if str(cart_items[i]['id']) == str(badminton_id) :
            del cart_items[i]
            break

    request.session['cart_items'] = cart_items

    return HttpResponseRedirect(reverse('cart_list',kwargs={}))

def cart_checkout(request) :
    try :
        cart_items = request.session.get('cart_items') 
        total_cart_price = request.session.get('cart_price') 
        
    except :
        pass
    

#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import Image
import requests
import qrcode

# def get_qr(mode="mobile", send_to="", amount=1.23):
#     url='https://thq68saavk.execute-api.ap-southeast-1.amazonaws.com/api/thai_qr'
#     r = requests.post(url, json={"mode":mode,"send_to":send_to, "amount":amount})
#     code=r.json()['result']
#     return code


# # In[2]:


# #to promptpay mobile
# code=get_qr(mode="mobile", send_to="09876543210", amount=1.23)
# print(code)
# img = qrcode.make(code,box_size=4)
# img.save('qr.png')
# Image(filename='qr.png') 


# # In[3]:


# #to promptpay nid
# code=get_qr(mode="nid", send_to="32109876543210", amount=1.23)
# print(code)
# img = qrcode.make(code,box_size=4)
# img.save('qr.png')
# Image(filename='qr.png') 
