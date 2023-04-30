from django.forms import ModelForm, models
from django import forms
from product.models import Product
from .models import SellerReport


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price', 'quantity']

class SellerReportForm(forms.ModelForm):
    class Meta:
        model = SellerReport
        fields = ['reason']