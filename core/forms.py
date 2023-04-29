from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import EmailValidator


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email', validators=[EmailValidator()])
    class Meta:
        model = AuthenticationForm