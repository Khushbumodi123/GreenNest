# urls.py
from django.urls import path
from . import views
from .middlewares.auth import  auth_middleware

app_name = 'landingPage'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('shop-detail/', views.shop_detail, name='shop_detail'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('404/', views.page_404, name='page_404'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('cart/', auth_middleware(views.cart) , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('orders/', auth_middleware(views.order), name='orders'),
]
