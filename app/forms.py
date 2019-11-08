from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.files.uploadedfile import UploadedFile


class SignUp(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, required=False, help_text='Required. Inform a valid email address.')
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image',)

    # def __init__(self, *args, **kwargs):
    #     super(SignUp, self).__init__(*args, **kwargs)
    #     self.fields['password1'].required = False
    #     self.fields['password2'].required = False
    #     self.fields['username'].required = False
    # def is_valid(self):
    #     return True;


class SignIn(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

class ContactUs(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    text = forms.CharField(max_length=250, min_length=10, required=True)
    email = forms.EmailField(required=True)

