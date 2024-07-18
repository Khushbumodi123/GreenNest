# urls.py
from django.urls import path
from . import views
from .middlewares.auth import  auth_middleware

app_name = 'landingPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.page_404, name='page_404'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('cart/', auth_middleware(views.cart) , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('orders/', auth_middleware(views.order), name='orders'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('search/', views.search, name='search'),
    #path('order/<int:order_id>/', auth_middleware(views.order_detail), name='order_detail'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_cart_quantity/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('userProfile/', views.profileTemp, name='user_profile'),
    path('about-us/', views.about_us, name='about_us'),
    path('privacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('terms-conditions/', views.terms_conditions, name='terms_conditions'),
    path('return-policy/', views.return_policy, name='return_policy'),
    path('faqs-help/', views.faqs_help, name='faqs_help'),
]
