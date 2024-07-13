from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import Category, Product, Customer, Order
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm

def index(request):
    products = Product.objects.all()
    return render(request, 'landingPage/index.html', {'products' : products})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landingPage:login')
    else:
        form = SignupForm()
    return render(request, 'landingPage/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                print("Login Successful")
                login(request, user)
                return redirect('landingPage:index')
            else:
                return render(request, 'landingPage/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'landingPage/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('landingPage:login')

def category_products(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id)

    search_query = request.GET.get('search')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rating_query = request.GET.get('rating')

    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__contains=search_query)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if rating_query:
        products = products.filter(rating__gte=rating_query)

    context = {
        'categories': categories,
        'products': products,
        'category_id': category_id
    }

    return render(request, 'landingPage/shop.html', context)

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    search_query = request.GET.get('search')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rating_query = request.GET.get('rating')

    if search_query:
        products = products.filter(name__icontains=search_query) | products.filter(description__contains=search_query)
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if rating_query:
        products = products.filter(rating__gte=rating_query)
    context = {
        'categories': categories,
        'products': products,
        'category_id': None
    }

    return render(request, 'landingPage/shop.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'landingPage/product.html')

def cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request , 'cart.html' , {'products' : products} )
    

def checkout(request):
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    customer = request.session.get('customer')
    cart = request.session.get('cart')
    products = Product.get_products_by_id(list(cart.keys()))
    print(address, phone, customer, cart, products)

    for product in products:
        print(cart.get(str(product.id)))
        order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
        order.save()
    request.session['cart'] = {}

    return redirect('cart')


def testimonial(request):
    """View function for rendering the testimonial page."""
    return render(request, 'testimonial.html')

def page_404(request, exception):
    """View function for rendering the 404 page."""
    return render(request, '404.html')

def contact(request):
    """View function for rendering the contact page."""
    return render(request, 'landingPage/contact.html')

def product_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'landingPage/product_list.html', context)

def order(request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'landinPage/index.html', data)




