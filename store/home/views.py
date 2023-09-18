from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from datetime import datetime
from home.models import contact,Product,Order,Customer
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group
from django.contrib.auth import logout,authenticate,login
from math import ceil
from django.http import JsonResponse
import json


# Create your views here.
def index(request):
     products = None
     products=Product.objects.all()
     product=request.POST.get('product')
     cart = request.session.get('cart',{})
     if product is not None:
          quantity=cart.get(product,0)
          
          if quantity:
            cart[product]= quantity+1 
          else:
            cart[product]=1
          items= request.POST.get("items",0)
          if int(items)>0:
            print(items)
            cart[product]=quantity+int(items)
            
               
    #  else:
    #       cart={}
    #       cart[product]=1
     request.session['cart']=cart
     print(cart)
     print(request.user)

     

     if request.user.is_anonymous:
        return redirect("/login")
     return render(request,'index.html',{'products': products})
    
def loginUser(request):
    print(request.user)
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
    # No backend authenticated the credentials
            return render(request,'login.html') 
    return render(request,'login.html') 
    
          
def logoutUser(request):
    if request.user.is_authenticated:

        logout(request)
        return redirect('/login')
    
    #return HttpResponse("this is home page")
def signup(request):
    if request.method=='POST':
        name=request.POST.get('Name')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        print(name)
        user = User.objects.create(username = name,email = email)
        user.set_password(password)
        user.save()
        # group = Group.objects.get(name="customer")
        # user.groups.add(group)


        # validation
        # value = {
        #     'first_name': fname,
        #     'last_name': lname,
        #     'phone': phone,
        #     'email': email
        # }
        customer=Customer(u_name=name,password=password,email=email,phone=phone)
        customer.user = user  

        customer.register()
        return redirect('login')

    return render(request,'signup.html')
def about(request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)

        return render(request,'about.html',{'products':products})

 
def Contact(request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        if request.method == "POST":
               name=request.POST.get('name')
               email=request.POST.get('email')
               phone=request.POST.get('phone')
               desc=request.POST.get('desc')
               Contact=contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
               Contact.save()
               messages.success(request, "Message sent successfully !")

               
        return render(request,'Contact.html',{'products':products})

    #return HttpResponse("this is Contact page")
@login_required  
def Checkout(request):
     cart = request.session.get('cart')
     
     products = Product.get_products_by_id(list(cart.keys()))

     if request.method=='POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.user.customer
        print(address, phone, customer, cart, products)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=customer,
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            
            print(order.placeOrder())
        request.session['cart'] = {}

        return redirect('/')

     return render(request,"checkout.html",{'products':products})
def Products(request,my_id):
     ids=list(request.session.get('cart').keys())
     products=Product.get_products_by_id(ids)
     product=Product.objects.filter(id=my_id)
     print(product)
     return render(request,'Products.html',{'product':product[0],'products':products})
def bag(request):
       ids=list(request.session.get('cart').keys())
       products=Product.get_products_by_id(ids)
       cart=request.session.get('cart')
       print(products,cart)
       return render(request,'bag.html',{'products':products})

def update_cart(request, product_id, action):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', {})
    if action == 'add':
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    elif action == 'remove':
         if cart[str(product_id)] == 1:
            cart.pop(str(product_id))
         else:
            cart[str(product_id)] -= 1
    elif action =='pop':
        if product_id in cart:
            cart.pop(product_id)
         
    request.session['cart'] = cart
    return redirect('/bag') 





@login_required
def OrderView(request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        customer = request.user.customer
        orders = Order.get_orders_by_customer(customer)
        print(customer,orders)
        return render(request , 'orders.html'  , {'orders' : orders,'products':products})