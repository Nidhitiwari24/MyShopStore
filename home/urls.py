from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("inndex", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("cards", views.cards, name='cards'), 
    path("cardss", views.cardss, name='cardss'),
    path("razorpay/templets/index", views.cardss, name='index'), 
]