from django.urls import path
from django.contrib import admin

from app import views

urlpatterns = [
    path('', views.navbar, name='home'),
    path('register/', views.sign_up, name='register'),
    path('logout/', views.logout_request),
    path('login/', views.login_request, name='login'),
    path('contact_us/', views.contact_us, name='contact'),
    path('contact_us2/', views.contact_us2),
    path('panel/', views.user_panel),
    path('profile/', views.profile),
    path('setting/', views.setting, name='setting'),
    path('makecourse/', views.make_course, name='makecourse'),
]