from django.http import HttpResponse
from django.shortcuts import render

def store(request):
    context = {}
    return render(request,'myapp/store.html', context)

def cart(request):
    context = {}
    return render(request,'myapp/cart.html', context)

def checkout(request):
    context = {}
    return render(request,'myapp/checkout.html', context)

