from django.shortcuts import render
#from .forms import RegistrationForm
from django.shortcuts import render, redirect
from product.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')

def login(request):
    text =  reverse("login.html")
    return render(text)

#remove later
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
            messages.error(request, 'Invalid username or password')
            return render(request, 'core/login.html', {'form': form})
    else:
        # Render the login form here
        form = AuthenticationForm()
        return render(request, 'core/login.html', {'form': form})
