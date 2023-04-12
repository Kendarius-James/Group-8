from django.contrib import admin

# Register your models here.

from .models import Category, Product, ReviewRating

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ReviewRating)