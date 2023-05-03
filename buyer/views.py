from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#added trying to get buyeruser to work
from accounts.models import BuyerProfile
##
from order.models import Order
from accounts.forms import CustomUserCreationForm
from accounts.forms import BuyerUserCreationForm
##
# Converting Title into Slug
from django.utils.text import slugify
from verify_email.email_handler import send_verification_email

def buyers(request):
    return render(request, 'buyer/buyers.html')


def become_buyer(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = BuyerUserCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.role='buyer'
            user.save()

            buyer_profile=profile_form.save(commit=False)
            buyer_profile.user = user
            buyer_profile.save()

            login(request, user)
            #might need to remove buyer = buyer.objects.create
            #buyer = buyer.objects.create(email=user.email,address=user.address,phonenumber=user.phone_number,company_description=user.company_description, created_by=user)

            if user_form.is_valid():

                inactive_user = send_verification_email(request, user_form)
                print (inactive_user)

        return redirect('core:home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = BuyerUserCreationForm() 

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'buyer/become_buyer.html', context)

@login_required
def edit_buyer(request):
    if request.user.role != 'buyer':
        return redirect('core:home') 

    buyer_profile = request.user.buyerprofile
    if request.method == 'POST':
        form = BuyerUserCreationForm(request.POST, instance=buyer_profile)
        if form.is_valid():
            form.save()
            request.user.save()
    else:
        form = BuyerUserCreationForm(instance=buyer_profile)

    context = {'form': form}

    return render(request, 'buyer/edit_buyer.html', context)

def buyers(request):
    buyers = BuyerProfile.objects.all()
    return render(request, 'buyer/buyers.html', {'buyers': buyers})

def buyer(request, buyer_id):
    buyer = get_object_or_404(BuyerProfile, pk=buyer_id)
    return render(request, 'buyer/buyer.html', {'buyer': buyer})

@login_required
def order_history(request):
    buyer = request.user.buyerprofile
    
    orders = Order.objects.filter(buyer=buyer).prefetch_related('items')

    # Filter items for each order
    for order in orders:
        order.filtered_items = order.items.all()

    return render(request, 'buyer/order_history.html', {'buyer': buyer, 'orders': orders})
