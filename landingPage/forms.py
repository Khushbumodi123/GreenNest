from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=15)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'phone', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
