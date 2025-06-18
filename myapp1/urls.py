from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [

    path('',views.home),
    path('register',views.register),
    path('showdata',views.showdata),
    path('delete',views.delete),
    path('update',views.update),
    path('saveupdate',views.saveupdate),
    path('login',views.login),
    path('checklogin',views.checklogin),
    path('dashboard',views.dashboard),
    path('logout',views.logout),
    path('file',views.file),
    path('savefile',views.savefile),
    path('cookies',views.cookies),
    path('getcookies',views.getcookies),
    path('form',views.form),
    path('multipledelete',views.multipledelete),
    path('customer/<int:id>',views.customerdetails),
    path('customerlist',views.list),

    path('send-otp/', views.send_otp),
    path('verify-otp/', views.verify_otp),



]
