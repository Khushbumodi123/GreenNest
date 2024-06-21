from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm

def store(request):
    context = {}
    return render(request,'myapp/store.html', context)

def cart(request):
    context = {}
    return render(request,'myapp/cart.html', context)

def checkout(request):
    context = {}
    return render(request,'myapp/checkout.html', context)

