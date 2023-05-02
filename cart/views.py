from django. conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from .cart import Cart
from .forms import CheckoutForm
from .models import ZipCode
from django.contrib.auth.models import AnonymousUser
from accounts.models import BuyerProfile, SellerProfile, CustomUser
from product.models import Product
from smtplib import SMTPAuthenticationError
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator

from order.utilities import checkout, notify_seller, notify_customer


def is_valid_zipcode(value):
    regex = r'^\d{5}(?:[-\s]\d{4})?$'
    validator = RegexValidator(regex)
    try:
        validator(value)
    except ValidationError:
        return False
    return True
        
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

                if not is_valid_zipcode(zipcode):
                    messages.error(request, 'Invalid zip code.')
                    return render(request, 'cart/cart.html', {'form': form, 'profile': profile, 'messages':messages.get_messages(request)})

                order = checkout(request, first_name, last_name, email, phone, address, zipcode, place, cart.get_total_cost())

                cart.clear()

                # Send Email Notification
                try:
                    notify_customer(order)
                    notify_seller(order)
                except SMTPAuthenticationError as e:
                    # Log the error and proceed with the checkout process
                    print(f"Error sending email: {e}")
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
        product = Product.objects.get(pk=change_quantity)
        current_cart_quantity = cart.cart.get(change_quantity, {}).get('quantity', 0)
        desired_new_quantity = int(quantity) + current_cart_quantity
        if desired_new_quantity <= product.quantity:
            cart.add(change_quantity, quantity, True)
        else:
            messages.error(request, 'The quantity you have requested is not available.')
        return redirect('cart:cart')

    return render(request, 'cart/cart.html', {'form': form, 'profile': profile, 'messages':messages.get_messages(request)})


def success(request):
    return render(request, 'cart/success.html')

