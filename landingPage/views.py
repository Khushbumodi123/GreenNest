from django.shortcuts import render

def index(request):
    """View function for rendering the landing page."""
    return render(request, 'landingPage/index.html')

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
