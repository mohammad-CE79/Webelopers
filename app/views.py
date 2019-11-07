from django.shortcuts import render

def navbar(request):
    return render(request, 'main/home.html')

def sign_in(request):
    return render(request, 'main/register.html')