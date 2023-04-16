from . import views
from .views import clear_comparison
from django.urls import path
from .views import report_product


app_name = 'product'


urlpatterns = [
    path('update_product/<int:product_id>/', views.update_product, name='update_product'),
    path('get_product_name/<int:product_id>/', views.get_product_name, name='get_product_name'),
    path('compare/clear/', clear_comparison, name='compare-clear'),
    path('remove_compare/<int:product_id>/', views.remove_compare, name='remove_compare'),
    path('compare/<int:product_id>/', views.compare, name='compare'),
    path('search', views.search, name="search"),
    path('product/report_product/<int:product_id>/', views.report_product, name='report_product'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product, name="product"),
    path('<slug:category_slug>/', views.category, name="category"),

]
