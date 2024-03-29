from cart.cart import Cart

from django.conf import settings
# for HTML Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    # Initialize buyer and seller as None
    buyer, seller = None, None

    # Check user's role and set the respective profile
    if request.user.role == 'buyer':
        buyer = request.user.buyerprofile
        seller = None
    else:
        buyer = None
        seller = request.user.sellerprofile

    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount, buyer=buyer, seller=seller)

    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], seller=item['product'].seller, price=item['product'].price, quantity=item['quantity'], item_name = item['product'].title, user=request.user)
        order.sellers.add(item['product'].seller)

        # Decrease the product quantity
        product = item['product']
        product.quantity -= item['quantity']
        product.save()
        
    return order

def notify_seller(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    for seller in order.sellers.all():
        to_email = seller.user.email
        subject = 'New order'
        text_content = 'You have a new order!'
        html_content = render_to_string('order/email_notify_seller.html', {'order': order, 'seller': seller})

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

def notify_customer(order):
    from_email = settings.DEFAULT_EMAIL_FROM

    to_email = order.email
    subject = 'Order confirmation'
    text_content = 'Thank you for the order!'
    html_content = render_to_string('order/email_notify_customer.html', {'order': order})

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()