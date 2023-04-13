from django.urls import path

#from .views import RegistrationForm

from . import views
#from core.views import login_redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('password_reset_done.html', RegistrationForm),
    path('password_reset_complete/login/', views.login_redirect, name="login"),
    #path('login/', views.login_redirect, name="login"),

    path('password_reset_form/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_form"),
    #path('password_change_form/', auth_views.PasswordChangeView.as_view(), name="password_change_form"),
    #Change password done, page shown after user change their password
    #The page shown after a user has been emailed a link to reset their password. 
    
    #This view is called by default if the PasswordResetView doesn't have an explicit success_url URL set.
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    
    #Presents a form for entering a new password.
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),

    
    #Presents a view which informs the user that the password has been successfully changed.
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
    
    path('login/', views.login, name="login")
    
]