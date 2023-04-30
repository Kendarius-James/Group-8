from django.db import models
from accounts.models import CustomUser, SellerProfile
# Create your models here.
class SellerReport(models.Model):
    
    seller = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
