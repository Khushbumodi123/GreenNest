from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path("", views.store, name='store'),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, name='checkout'),
]