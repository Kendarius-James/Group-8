from django import forms
from django.forms.fields import IntegerField
from django.forms.forms import Form
from .models import ReviewRating

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']