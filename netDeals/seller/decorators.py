from functools import wraps
from django.contrib.auth.decorators import user_passes_test
from .utils import is_approved_seller
from accounts.models import SellerProfile
from django.shortcuts import redirect

def is_seller_approved(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        seller = SellerProfile.objects.get(user=request.user)
        if seller.is_approved:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('seller:restricted_access')
    return _wrapped_view