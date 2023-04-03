from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'seller'


urlpatterns = [
    path('', views.sellers, name="sellers"),
    path('become-seller/', views.become_seller, name="become-seller"),
    path('seller-dashboard/', views.seller_dashboard, name="seller-dashboard"),
    path('edit-seller/', views.edit_seller, name="edit-seller"),

    path('add-product/', views.add_product, name="add-product"),

    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='seller/login.html'), name="login"),

    path('<int:seller_id>/', views.seller, name="seller"),
    

    #path('password_reset_form/', views.passw, name='password_reset_form'),

    path('password_reset_form/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]
#accounts/reset/<uidb64>/<token>/

#reset/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/