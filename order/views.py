from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem, Product

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json

# Create your views here.
@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, seller=request.user.sellerprofile)
   
    try:
        order.delete()
    except Exception as e:
        print(f"Error deleting product: {e}")
        return JsonResponse({'status': 'error', 'message': 'Error deleting product'})

    return JsonResponse({'status': 'success'})

def seller_return_status(request, order_id, product_id):
    order = get_object_or_404(OrderItem, order_id=order_id, product_id=product_id)
    order.return_status = True
    order.save()
    
    return JsonResponse({'status': 'success'})
    #return HttpResponseRedirect('/order_history/')

def buyer_return_status(request, order_id, product_id):
    order = get_object_or_404(OrderItem, order_id=order_id, product_id=product_id)
    order.return_status = True
    #order.product.pk 
    order.save()
    
    return JsonResponse({'status': 'success'})
    #return HttpResponseRedirect('/order_history/')
