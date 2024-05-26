from django.contrib import admin
from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile',views.profile,name= 'profile'),
    path('contact',views.Contact,name= 'contact'),
    path('checkout/',views.checkout,name= 'Checkout'),
    path('handlerequest/',views.handlerequest,name= 'HandleRequest'),
  
]