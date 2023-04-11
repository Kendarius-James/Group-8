from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.apps import apps

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='buyer')
   
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class BuyerProfile(models.Model):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class SellerProfile(models.Model):
    is_approved = models.BooleanField(default=False) # for admin approval
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    
    def get_balance(self):
        print("Called get_balance function")
        OrderItem = apps.get_model('order', 'OrderItem')
        items_sold = OrderItem.objects.filter(seller_id=self.id)
        print(f"Items sold: {items_sold}")  # Add this line
        total_balance = sum(item.price * item.quantity for item in items_sold)
        print(f"Total balance: {total_balance}")  # Add this line
        return total_balance


    # def get_paid_amount(self):
    #     items = self.items.filter(buyer_paid=True, order__buyers__in=[self.id])
    #     return sum((item.product.price * item.quantity) for item in items)
