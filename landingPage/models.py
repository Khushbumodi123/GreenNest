from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from .utils import one_year_from_today, validate_rating  

class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='customers/images/', default='customers/images/default.jpg')
    address = models.CharField(max_length=255, default="Not Provided")
    city = models.CharField(max_length=100, default="Not Provided")
    country = models.CharField(max_length=100, default="Not Provided")
    postal_code = models.CharField(max_length=20, default="Not Provided")


    objects = CustomerManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return None

# --------------Category Module -------------------
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Kitchen', 'Kitchen'),
        ('Bathroom', 'Bathroom'),
        ('Cleaning', 'Cleaning'),
        ('Decor', 'Decor'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES,unique=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name


# --------------Product Module -------------------
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=100)
    image = models.ImageField(upload_to='products/images/')
    brand = models.CharField(max_length=255, default='')
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expiration_date = models.DateField(default=one_year_from_today)
    rating = models.PositiveIntegerField(validators=[validate_rating], null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

# --------------Order Module -------------------
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50, default='')
    province = models.CharField(max_length=50, default='')  
    postcode = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=15, default='')
    email = models.EmailField(default='default@example.com')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Order {self.id} by {self.customer.email}'

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

