from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from .models import Category, Product, Customer, Order
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import  check_password

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    print(products[0].image.url)
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



class Signup(View):
    def get(self, request):
        return render(request, 'landingPage/signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'landingPage/signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'landingPage/login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'landingPage/login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')



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




