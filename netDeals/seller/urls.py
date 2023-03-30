from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'seller'


urlpatterns = [
    path('', views.sellers, name="sellers"),
    path('become-seller/', views.become_seller, name="become-seller"),
    path('seller-admin/', views.seller_admin, name="seller-admin"),
    path('edit-seller/', views.edit_seller, name="edit-seller"),

    path('add-product/', views.add_product, name="add-product"),

    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='seller/login.html'), name="login"),

    path('<int:seller_id>/', views.seller, name="seller"),
]
