from django.contrib import admin
from django.urls import path
from authcart import views

urlpatterns = [
    path('signup/',views.signup,name= 'signup.html'),
    path('login/',views.handlelogin,name= 'handlelogin.html'),
    path('logout/',views.handlelogout,name= 'handlelogout.html'),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate'),
    path('request-reset-email/',views.RequestResetEmailView.as_view(),name='request-reset-email'),
    path('set-new-password/<uidb64>/<token>',views.SetNewPasswordView.as_view(),name='set-new-password'),
  
]