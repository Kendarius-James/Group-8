from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'


urlpatterns = [
    path('login/', views.login_redirect, name="login"),
    #path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path('', views.frontpage, name="home"),
    path('contact-us/', views.contactpage, name="contact"),
]
