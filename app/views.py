from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect


def navbar(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"new account created : {username}")
            login(request, user)
            return redirect("/")

        else:
            return HttpResponse('asdfadsf')
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request=request,
                          template_name='main/register.html',
                          context={"form": form})

    form = UserCreationForm
    return render(request=request,
                  template_name='main/register.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")
