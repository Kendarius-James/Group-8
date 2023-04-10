from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'buyer'


urlpatterns = [
    path('', views.buyers, name="buyers"),
    path('become-buyer/', views.become_buyer, name="become-buyer"),
    # path('seller-admin/', views.seller_admin, name="seller-admin"),
    path('edit-buyer/', views.edit_buyer, name="edit-buyer"),

    # path('add-product/', views.add_product, name="add-product"),

    # path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    # path('login/', auth_views.LoginView.as_view(template_name='seller/login.html'), name="login"),

    # path('<int:seller_id>/', views.seller, name="seller"),
]
