from django import forms
from django.forms.fields import IntegerField
from django.forms.forms import Form
from .models import ProductReport, Rating

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class ProductReportForm(forms.ModelForm):
    class Meta:
        model = ProductReport
        fields = ['reason']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']