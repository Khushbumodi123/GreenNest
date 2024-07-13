# urls.py
from django.urls import path
from . import views
from .middlewares.auth import  auth_middleware

app_name = 'landingPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product-detail/', views.product_detail, name='product_detail'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.page_404, name='page_404'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:product_id>/<str:action>/', views.update_cart_quantity, name='update_cart_quantity'),
    path('checkout/', views.checkout , name='checkout'),
    path('orders/', auth_middleware(views.order), name='orders'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('password_reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    #path('order/<int:order_id>/', auth_middleware(views.order_detail), name='order_detail'),
]
