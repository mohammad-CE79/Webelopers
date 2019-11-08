from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import ListView

from app.forms import SignUp, SignIn, ContactUs
from app.models import CourseForm, Course


def navbar(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"new account created : {username}")
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
        return render(request=request,
                      template_name='main/register.html',
                      context={"form": form})

    form = SignUp()
    return render(request=request,
                  template_name='main/register.html',
                  context={"form": form})


def login_request(request):
    if request.method == 'POST':
        form = SignIn(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = SignIn()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def contact_us(request):
    if request.method == 'POST':
        form = ContactUs(request.POST)
        if form.is_valid():
            sendmail(request)
            return redirect('/contact_us2')

    return render(request, 'main/contact_us.html')


def contact_us2(request):
    return render(request, 'main/contact_us2.html')


def sendmail(request):
    subject = request.POST.get('title', '')
    message = request.POST.get('text', '')
    from_email = request.POST.get('email', '')
    message.join('\n' + from_email)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['webe19lopers@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)


def user_panel(request):
    return render(request, 'main/userpanel.html')


def setting(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        image = request.FILES('image')
        user = request.user

        if first_name != '':
            user.first_name = first_name
        if last_name != '':
            user.last_name = last_name
        user.image = image
        user.save()
        return redirect('/profile')
    else:
        return render(request, 'main/setting.html')


@login_required(login_url='/')
def profile(request):
    user = request.user
    return render(request, 'main/profile.html', context={"user": user})


def make_course(request):
    if request.method == 'POST':
        course = CourseForm(request.POST)
        if course.is_valid():
            course.save()
    return render(request, 'main/makecourse.html')

def all_courses(request):
    return render(request, 'main/all_courses.html', context={"course": Course.objects.all()})

class SearchResultsView(ListView):
    model = Course
    template_name = 'main/all_courses.html'
    extra_context = {"course": Course.objects.all()}

    def get_queryset(self):
        query = self.request.GET.get('search_query')
        object_list = Course.objects.filter(
            Q(department=query)
        )
        return object_list

