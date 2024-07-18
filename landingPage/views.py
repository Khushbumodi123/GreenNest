from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Customer, Order
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, PasswordResetForm, SetPasswordForm, OrderForm


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
                request.session['customer'] = user.id
                login(request, user)
                return redirect('landingPage:index')
            else:
                return render(request, 'landingPage/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'landingPage/login.html', {'form': form})

def logout_view(request):
    logout(request)
    if 'customer' in request.session:
        del request.session['customer']
    return redirect('landingPage:index')

def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = Customer.objects.filter(email=email).first()
            if user:
                request.session['reset_email'] = email
                return redirect('landingPage:password_reset_confirm')
            else:
                return render(request, 'landingPage/password_reset.html', {'form': form, 'error': 'Email not found.'})
    else:
        form = PasswordResetForm()
    return render(request, 'landingPage/password_reset.html', {'form': form})

def password_reset_confirm(request):
    email = request.session.get('reset_email')
    if not email:
        return redirect('landingPage:password_reset')

    user = Customer.objects.filter(email=email).first()
    if not user:
        return redirect('landingPage:password_reset')

    if request.method == "POST":
        form = SetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            user.set_password(new_password)
            user.save()
            return redirect('landingPage:login')
    else:
        form = SetPasswordForm()
    return render(request, 'landingPage/password_reset_confirm.html', {'form': form})

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

def search(request):
    query = request.GET.get('query')
    search_history = request.COOKIES.get('search_history', '')

    if query:
        products = Product.objects.filter(name__icontains=query)

        # Update search history
        if search_history:
            search_history_list = search_history.split('|')
            if query not in search_history_list:
                search_history_list.append(query)
            search_history = '|'.join(search_history_list[-5:])  # Limit history to last 5 searches
        else:
            search_history = query
    else:
        products = Product.objects.none()

    response = render(request, 'landingPage/search_results.html', {'products': products, 'query': query, 'search_history': search_history.split('|') if search_history else []})

    # Set the updated search history in the cookies
    response.set_cookie('search_history', search_history, max_age=30*24*60*60)  # Cookie expires in 30 days

    return response

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
    categories = Category.objects.all()
    return render(request, 'landingPage/product.html', {'product': product, 'categories': categories})


def cart(request):
    if not request.session.get('cart'):
        request.session['cart'] = {}
    cart = request.session.get('cart')
    product_ids = list(cart.keys())
    products = Product.get_products_by_id(product_ids)
    context = {
        'products': products,
        'cart': cart
    }
    return render(request, 'landingPage/cart.html', context)

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = cart.get(str(product_id), 0)
    cart[str(product_id)] = quantity + 1
    request.session['cart'] = cart
    return redirect('landingPage:cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('landingPage:cart')

def update_cart_quantity(request, product_id, action):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        if action == 'increment':
            cart[str(product_id)] += 1
        elif action == 'decrement':
            cart[str(product_id)] -= 1
            if cart[str(product_id)] == 0:
                del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('landingPage:cart')

@login_required(login_url='landingPage:login')
def checkout(request):
    customer_id = request.user.id
    if not customer_id:
        return redirect('landingPage:login')

    cart = request.session.get('cart', {})
    products = Product.get_products_by_id(list(cart.keys()))

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            for product in products:
                order = form.save(commit=False)
                order.customer = Customer.objects.get(id=customer_id)
                order.product = product
                order.quantity = cart.get(str(product.id))
                order.price = product.price
                order.save()
            request.session['cart'] = {}
            return redirect('landingPage:cart')
    else:
        form = OrderForm()

    context = {
        'form': form,
        'products': products,
        'cart': cart
    }

    return render(request, 'landingPage/checkout.html', context)

def testimonial(request):
    """View function for rendering the testimonial page."""
    return render(request, 'testimonial.html')

def page_404(request, exception):
    """View function for rendering the 404 page."""
    return render(request, '404.html')

def contact(request):
    if request.method == 'POST':
        return redirect('landingPage:index')
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

@login_required(login_url='login')
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    return redirect('landingPage:product_detail', product_id=product_id)

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]
    request.session['cart'] = cart
    return redirect('landingPage:product_detail', product_id=product_id)


def profileTemp(request):
    if request.user.is_authenticated:
        #customer = Customer.get_customer_by_email(request.user.email)
        print(request.user.email)
        #print(customer)
        #if customer:
        #return render(request, 'profile_page/profile1.html', {'customer': customer})
        return HttpResponse(request.user.email)
    else:
        return HttpResponse("not!")





