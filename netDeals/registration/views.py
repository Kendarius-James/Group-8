from django.shortcuts import render
from .forms import RegistrationForm

def password_reset_form (request):
    context = {}
    context['form'] = RegistrationForm()
    return render( request, "password_reset_form.html", context)