from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('allergy/',views.allergy,name='allergy'),
    path('contact/',views.contact,name='contact'),
    path('menu',views.menu,name='menu'),
    path('services/',views.services,name='services'),
    path('foodmenu/',views.foodmenu,name='foodmenu'),
    path('contact/',views.contact,name='contact'),

]