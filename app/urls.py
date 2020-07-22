from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about-us'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('career/', views.career, name='career'),

]
