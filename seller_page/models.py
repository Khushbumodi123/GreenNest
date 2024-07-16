from django.db import models
from landingPage.models import Customer

class Seller(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='product_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
