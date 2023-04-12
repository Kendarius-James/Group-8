from django.shortcuts import render
from product.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    products = Product.objects.all()
    context = {
        'newest_products': newest_products,
        'products': products,
    }
    return render(request, 'core/frontpage.html', context)


def contactpage(request):
    return render(request, 'core/contact.html')

def login_redirect(request):
    form = AuthenticationForm()
    invalid_email = False

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            validate_email(username)
        except ValidationError:
            invalid_email = True
            messages.warning(request, 'Invalid email format')

        if not invalid_email:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return HttpResponseRedirect(reverse('admin:index'))
                else:
                    return HttpResponseRedirect(reverse('core:home'))
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'core/login.html', {'form': form})