from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls
app_name = 'core'


urlpatterns = [
    path('login/', views.login_redirect, name="login"),
    #path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('', views.frontpage, name="home"),
    path('contact-us/', views.contactpage, name="contact"),

    path('password_reset_form/', auth_views.PasswordResetView.as_view(), name="password_reset_form"),
    
    
    
    #Changes the password, Create new page (Allows a user to change their password.)
    ####path('password_change_form/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    #Change password done, page shown after user change their password
    #The page shown after a user has been emailed a link to reset their password. 
    #This view is called by default if the PasswordResetView doesn't have an explicit success_url URL set.
    ###path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #Presents a form for entering a new password.
    ###path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #Presents a view which informs the user that the password has been successfully changed.
    ###path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
