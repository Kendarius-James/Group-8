from django.urls import path

from .views import RegistrationForm

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('password_reset_done.html', RegistrationForm),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

]