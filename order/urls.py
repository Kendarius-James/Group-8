from django.urls import path
from . import views

app_name = 'order'


urlpatterns = [
    path('delete_order/<int:order_id>', views.delete_order, name='delete_order'),
    path('seller_return_status/<int:order_id>/<int:product_id>/return/', views.seller_return_status, name='seller_return_status'),
    path('buyer_return_status/<int:order_id>/<int:product_id>/return/', views.buyer_return_status, name='buyer_return_status'),
    #path('delete_order/<str:order_date>', views.return_date, name='order_date'),
]
