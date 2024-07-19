from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from landingPage.models import Category
from .forms import ProductForm

def add_product(request):
    categories = Category.objects.all()  # Fetch all categories
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user.seller  # Assuming the user is already linked to a seller
            product.save()
            return redirect('seller_products')
    else:
        form = ProductForm()

    return render(request, 'seller_page/add_prduct.html', {'form': form, 'categories': categories})
def seller_products(request):
    products = Product.objects.filter(seller=request.user.seller)
    return render(request, 'seller_page/seller_products.html', {'products': products})
