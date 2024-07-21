from django.urls import path
from . import views

app_name = 'seller_page'

urlpatterns = [
    path('add-product/', views.add_product, name='add_product'),
    path('seller-products/', views.seller_products, name='seller_products'),
]
