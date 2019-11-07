from django.urls import path
from django.contrib import admin

from app import views

urlpatterns = [
    path('', views.navbar),
    path('register/', views.sign_in),
    path('logout/', views.logout_request),
]