from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BuyerProfile, SellerProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
<<<<<<< Updated upstream
        fields = ('email', 'role', 'phone_number', 'address')
=======
        fields = ('email', 'role',)
>>>>>>> Stashed changes

class BuyerUserCreationForm(forms.ModelForm):
    class Meta:
        model = BuyerProfile
<<<<<<< Updated upstream
        fields = ('first_name', 'last_name')
=======
        fields = ('first_name', 'last_name', 'phone_number', 'address')
>>>>>>> Stashed changes

class SellerUserCreationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False)
    address = forms.CharField(max_length=255, required=False)
    class Meta:
        model = SellerProfile
        fields = ('company_name', 'company_description', 'phone_number', 'address')