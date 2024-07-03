from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'landingPage/index.html', context)

def category_products(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'categories': Category.objects.all(),
        'products': products,
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

