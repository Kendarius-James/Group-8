from django.contrib import admin
from accounts.models import CustomUser
from django.shortcuts import redirect
from .models import SellerProfile
# Register your models here.
admin.site.register(CustomUser)
#approve new sellers
def approve_seller(request, seller_id):
    if request.user.is_superuser:
        seller = SellerProfile.objects.get(id=seller_id)
        seller.is_approved = True
        seller.save()
    return redirect('manage_seller_approvals')