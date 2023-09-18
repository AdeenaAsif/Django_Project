from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [

    path("",views.index, name='home'),
    path("login",views.loginUser, name='login'),
    path("logout",views.logoutUser, name='logout'),
    path("about",views.about, name='about'),
   # path("services",views.services, name='services'),
    path("Contact",views.Contact, name='Contact'),
    path("Checkout",views.Checkout,name='Checkout'),
    path("Products/<int:my_id>",views.Products, name='Products'),
    path("bag",views.bag, name='bag'),
    path("signup",views.signup, name='signup'),
    path('update_cart/<str:product_id>/<str:action>/', views.update_cart, name='update_cart'),
    path("orders",views.OrderView,name='OrderView'),






]
