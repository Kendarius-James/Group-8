from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, BuyerProfile, SellerProfile
from django.core.exceptions import ValidationError
import re
from django.contrib import messages

def validate_phone_number(phone_number):
    # Define the regex pattern for a valid phone number
    pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

    # Use the regex pattern to match the phone number
    match = re.match(pattern, phone_number)
    if match:
        return True
    else:
        return False

class PhoneNumberFormField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if not validate_phone_number(value):
            raise ValidationError("Please enter a valid phone number")
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class BuyerUserCreationForm(forms.ModelForm):
    phone_number = PhoneNumberFormField()
    class Meta:
        model = BuyerProfile
        fields = ('first_name', 'last_name', 'phone_number', 'address')

class SellerUserCreationForm(forms.ModelForm):
    phone_number = PhoneNumberFormField(required=False)
    address = forms.CharField(max_length=255, required=False)
    class Meta:
        model = SellerProfile
        fields = ('company_name', 'company_description', 'phone_number', 'address')