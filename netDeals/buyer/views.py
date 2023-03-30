<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#added trying to get buyeruser to work
from accounts.models import SellerProfile
##
from accounts.forms import CustomUserCreationForm
from accounts.forms import BuyerUserCreationForm
##
# Converting Title into Slug
from django.utils.text import slugify

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

            return redirect('core:home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = BuyerUserCreationForm() 

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'seller/become_seller.html', context)
>>>>>>> Stashed changes
