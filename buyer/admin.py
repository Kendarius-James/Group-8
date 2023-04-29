from django.contrib import admin
from accounts.models import BuyerProfile
# Register your models here.
class BuyerProfileAdmin(admin.ModelAdmin):
    list_display = ('user',) # Add other fields you want to display
admin.site.register(BuyerProfile, BuyerProfileAdmin)