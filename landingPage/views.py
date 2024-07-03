from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from .models import Category


def index(request):
    categories = Category.objects.all()  # Fetch all categories from database
    context = {
        'categories': categories
    }
    return render(request, 'landingPage/index.html', context)

def shop(request):
    """View function for rendering the shop page."""
    return render(request, 'shop.html')

def shop_detail(request):
    """View function for rendering the shop detail page."""
    return render(request, 'shop_detail.html')

def cart(request):
    """View function for rendering the cart page."""
    return render(request, 'cart.html')

def checkout(request):
    """View function for rendering the checkout page."""
    return render(request, 'checkout.html')

def testimonial(request):
    """View function for rendering the testimonial page."""
    return render(request, 'testimonial.html')

def page_404(request, exception):
    """View function for rendering the 404 page."""
    return render(request, '404.html')

def contact(request):
    """View function for rendering the contact page."""
    return render(request, 'contact.html')

def product_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'landingPage/product_list.html', context)

