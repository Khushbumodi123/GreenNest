from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-sm',
        'placeholder': 'example@gmail.com',
        'id': 'email'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-sm',
        'placeholder': '********',
        'id': 'password'
    }))

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control me-2',
        'placeholder': 'Search',
        'aria-label': 'Search'
    }))
