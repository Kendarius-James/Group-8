from django. conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from .cart import Cart
from .forms import CheckoutForm
from django.contrib.auth.models import AnonymousUser
from accounts.models import BuyerProfile, SellerProfile, CustomUser

from order.utilities import checkout, notify_seller, notify_customer
def cart_detail(request):
    cart = Cart(request)

    if isinstance(request.user, AnonymousUser) or request.user.role not in ['buyer', 'seller']:
        profile = None
    elif request.user.role == 'buyer':
        profile = BuyerProfile.objects.get(user=request.user)
    else:
        profile = SellerProfile.objects.get(user=request.user)
    
    if request.method == 'POST':

        form = CheckoutForm(request.POST)
        if form.is_valid():

                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                address = form.cleaned_data['address']
                zipcode = form.cleaned_data['zipcode']
                place = form.cleaned_data['place']

                order = checkout(request, first_name, last_name, email, phone, address, zipcode, place, cart.get_total_cost())

                cart.clear()

                # SEnd Email Notification
                notify_customer(order)
                notify_seller(order)

                return redirect('cart:success')
                
    else:
        form = CheckoutForm()

    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart:cart')
    
    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart:cart')
        
    return render(request, 'cart/cart.html', {'form': form, 'profile': profile})


def success(request):
    return render(request, 'cart/success.html')

