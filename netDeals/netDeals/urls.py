
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_redirect, name="login"),
    path('', include('core.urls')),
    path('buyer/', include('buyer.urls')),
    path('seller/', include('seller.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
