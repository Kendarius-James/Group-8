from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('login/', views.login_redirect, name="login"),
    path('', views.frontpage, name="home"),
    path('contact-us/', views.contactpage, name="contact"),
]
