from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import SellerUser

class SellerUserCreationForm(UserCreationForm):

    class Meta:
        model = SellerUser
        fields = ("username", "email", "address", "company_description","phonenumber")

class SellerUserChangeForm(UserChangeForm):

    class Meta:
        model = SellerUser
        fields = ("username", "email", "address", "company_description","phonenumber")