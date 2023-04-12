from . import views
from .views import clear_comparison
from django.urls import path



app_name = 'product'


urlpatterns = [
    path('get_product_name/<int:product_id>/', views.get_product_name, name='get_product_name'),
    path('compare/clear/', clear_comparison, name='compare-clear'),
    path('remove_compare/<int:product_id>/', views.remove_compare, name='remove_compare'),
    path('compare/<int:product_id>/', views.compare, name='compare'),
    path('search', views.search, name="search"),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name="product"),
    path('<slug:category_slug>/', views.category, name="category"),
    path('submit_review/<int:product_id>/', views.submit_review, name="submit_review"),
    
]
