from django.db import models
from django.db.models.fields.related import OneToOneField
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=30, blank=True)
    company_description = models.CharField(max_length=1024, blank=True)
    phonenumber=models.CharField(max_length=10,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_balance(self):
        items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)


# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models.fields.related import OneToOneField

# # Create your models here.

# class Vendor(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=30, blank=True)
#     company_description = models.CharField(max_length=1024, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    
#     class Meta:
#         ordering = ['name']
    
#     def __str__(self):
#         return self.name

#     def get_balance(self):
#         items = self.items.filter(vendor_paid=False, order__vendors__in=[self.id])
#         return sum((item.product.price * item.quantity) for item in items)

#     def get_paid_amount(self):
#         items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
#         return sum((item.product.price * item.quantity) for item in items)

