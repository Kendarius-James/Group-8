from django.db import models
from product.models import Product
from accounts.models import SellerProfile
from accounts.models import BuyerProfile


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    sellers = models.ManyToManyField(SellerProfile, related_name="orders")
    buyer = models.ForeignKey(BuyerProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='buyer_orders')
    seller = models.ForeignKey(SellerProfile, null=True, blank=True, on_delete=models.SET_NULL, related_name='seller_orders')



    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=50, default="Unknown")
    seller = models.ForeignKey(SellerProfile, related_name="items", on_delete=models.CASCADE)
    seller_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    return_status = models.BooleanField(default=False)

    def get_item_title(self):
        return self.item_name if self.product else self.item_name

    def get_item_price(self):
        return self.product.price if self.product else self.price
    
    def __str__(self):
        return str(self.id)

    def get_total_price(self):
        return self.price * self.quantity
