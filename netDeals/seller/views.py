<<<<<<< Updated upstream
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#added trying to get buyeruser to work
from accounts.models import SellerProfile
##
from accounts.forms import CustomUserCreationForm
from accounts.forms import SellerUserCreationForm
##
from product.models import Product
from .forms import ProductForm

# Converting Title into Slug
from django.utils.text import slugify

# Create your views here.
# SellerProfile = SellerProfile
# seller = seller
# sellers = sellers

def sellers(request):
    return render(request, 'seller/sellers.html')


def become_seller(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = SellerUserCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.role='seller'
            user.save()

            seller_profile=profile_form.save(commit=False)
            seller_profile.user = user
            seller_profile.save()

            login(request, user)
            #might need to remove seller = seller.objects.create
            #seller = seller.objects.create(email=user.email,address=user.address,phonenumber=user.phone_number,company_description=user.company_description, created_by=user)

            return redirect('core:home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = SellerUserCreationForm() 

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'seller/become_seller.html', context)


@login_required
def seller_admin(request):
    seller = request.user.sellerprofile
    products = seller.products.all()
    orders = seller.orders.all()
    for order in orders:
        order.seller_amount = 0
        order.seller_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.seller == request.user.sellerprofile:
                if item.seller_paid:
                    order.seller_paid_amount += item.get_total_price()
                else:
                    order.seller_amount += item.get_total_price()
                    order.fully_paid = False


    return render(request, 'seller/seller_admin.html', {'seller': seller, 'products': products, 'orders': orders})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False) # Because we have not given seller yet
            product.seller = request.user.sellerprofile
            product.slug = slugify(product.title)
            product.save() #finally save

            return redirect('seller:seller-admin')

    else:
        form = ProductForm

    return render(request, 'seller/add_product.html', {'form': form})


@login_required
def edit_seller(request):

    seller_profile = request.user.sellerprofile
    if request.method == 'POST':
        form = SellerUserCreationForm(request.POST, instance=seller_profile)
        if form.is_valid():
            form.save()

            request.user.phone_number = form.cleaned_data['phone_number']
            request.user.address = form.cleaned_data['address']
            request.user.save()
    else:
        initial_data = {
            'phone_number': request.user.phone_number,
            'address': request.user.address
        }
        form = SellerUserCreationForm(instance=seller_profile, initial=initial_data)

    context = {'form': form}

    return render(request, 'seller/edit_seller.html', context)

def sellers(request):
    sellers = SellerProfile.objects.all()
    return render(request, 'seller/sellers.html', {'sellers': sellers})

def seller(request, seller_id):
    seller = get_object_or_404(SellerProfile, pk=seller_id)
    return render(request, 'seller/seller.html', {'seller': seller})


# seller = request.user.seller

#     if request.method == 'POST':
#         name  = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         address = request.POST.ger('address', '')
#         company_description = request.POST.get('comany_description', '')
#         if name:
#             seller.created_by.email = email
#             seller.created_by.save()

#             vendor.name = name
#             vendor.save

#             return redirect('vendor:vendor-admin')

#     return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})
=======
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#added trying to get buyeruser to work
from accounts.models import SellerProfile
##
from accounts.forms import CustomUserCreationForm
from accounts.forms import SellerUserCreationForm
##
from product.models import Product
from .forms import ProductForm

# Converting Title into Slug
from django.utils.text import slugify

# Create your views here.
# SellerProfile = SellerProfile
# seller = seller
# sellers = sellers

def sellers(request):
    return render(request, 'seller/sellers.html')


def become_seller(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = SellerUserCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.role='seller'
            user.save()

            seller_profile=profile_form.save(commit=False)
            seller_profile.user = user
            seller_profile.save()

            login(request, user)
            #might need to remove seller = seller.objects.create
            #seller = seller.objects.create(email=user.email,address=user.address,phonenumber=user.phone_number,company_description=user.company_description, created_by=user)

            return redirect('core:home')
    else:
        user_form = CustomUserCreationForm()
        profile_form = SellerUserCreationForm() 

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'seller/become_seller.html', context)


@login_required
def seller_admin(request):
    seller = request.user.sellerprofile
    products = seller.products.all()
    orders = seller.orders.all()
    for order in orders:
        order.seller_amount = 0
        order.seller_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.seller == request.user.sellerprofile:
                if item.seller_paid:
                    order.seller_paid_amount += item.get_total_price()
                else:
                    order.seller_amount += item.get_total_price()
                    order.fully_paid = False


    return render(request, 'seller/seller_admin.html', {'seller': seller, 'products': products, 'orders': orders})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False) # Because we have not given seller yet
            product.seller = request.user.sellerprofile
            product.slug = slugify(product.title)
            product.save() #finally save

            return redirect('seller:seller-admin')

    else:
        form = ProductForm

    return render(request, 'seller/add_product.html', {'form': form})


@login_required
def edit_seller(request):

    seller_profile = request.user.sellerprofile
    if request.method == 'POST':
        form = SellerUserCreationForm(request.POST, instance=seller_profile)
        if form.is_valid():
            form.save()

            request.user.phone_number = form.cleaned_data['phone_number']
            request.user.address = form.cleaned_data['address']
            request.user.save()
    else:
        initial_data = {
            'phone_number': request.user.phone_number,
            'address': request.user.address
        }
        form = SellerUserCreationForm(instance=seller_profile, initial=initial_data)

    context = {'form': form}

    return render(request, 'seller/edit_seller.html', context)

def sellers(request):
    sellers = SellerProfile.objects.all()
    return render(request, 'seller/sellers.html', {'sellers': sellers})

def seller(request, seller_id):
    seller = get_object_or_404(SellerProfile, pk=seller_id)
    return render(request, 'seller/seller.html', {'seller': seller})


# seller = request.user.seller

#     if request.method == 'POST':
#         name  = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         address = request.POST.ger('address', '')
#         company_description = request.POST.get('comany_description', '')
#         if name:
#             seller.created_by.email = email
#             seller.created_by.save()

#             vendor.name = name
#             vendor.save

#             return redirect('vendor:vendor-admin')

#     return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})
>>>>>>> Stashed changes