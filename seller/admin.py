from django.contrib import admin
from accounts.models import SellerProfile

# admin.site.register(SellerProfile)
#
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_approved',) # Add other fields you want to display
    list_filter = ('is_approved',) # Filter by approval status
    actions = ['approve_sellers', 'disapprove_sellers']

    def approve_sellers(self, request, queryset):
        queryset.update(is_approved=True)

    approve_sellers.short_description = "Approve selected seller accounts"

    def disapprove_sellers(self, request, queryset):
        queryset.update(is_approved=False)
        
    disapprove_sellers.short_description = "Disapprove selected seller accounts"

admin.site.register(SellerProfile, SellerProfileAdmin)