from django.urls import path
from django.contrib import admin

from app import views

urlpatterns = [
    path('', views.navbar, name='home'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.logout_request),
    path('login/', views.login_request, name='login'),
    path('contact_us/', views.contact_us),
]