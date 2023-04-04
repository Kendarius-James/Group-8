from django.shortcuts import render
from product.models import Product
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    context = {
        'newest_products': newest_products,
    }
    return render(request, 'core/frontpage.html', context)


def contactpage(request):
    return render(request, 'core/contact.html')

def login_redirect(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                # Redirect to the appropriate page for other user roles
                return HttpResponseRedirect(reverse('core:home'))
        else:
            # Handle failed authentication here
            pass
    else:
        # Render the login form here
        pass