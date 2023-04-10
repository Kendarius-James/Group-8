from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from core.views import login_redirect



app_name = 'seller'


urlpatterns = [
    path('login/', login_redirect, name="login"),
    path('', views.sellers, name="sellers"),
    path('restricted_access/', views.restricted_access, name='restricted_access'),
    path('become-seller/', views.become_seller, name="become-seller"),
    path('seller-dashboard/', views.seller_dashboard, name="seller-dashboard"),
    path('edit-seller/', views.edit_seller, name="edit-seller"),
    path('add-product/', views.add_product, name="add-product"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('<int:seller_id>/', views.seller, name="seller"),
]
