# might not need this, https://learndjango.com/tutorials/django-custom-user-model says
# Admin is highly coupled to the default User model implying that the admin user would need
# the same parameters as the new one but that does not fit our use case since admin does not need
# to store address, etc



# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# from .forms import BuyerUserCreationForm, BuyerUserChangeForm
# from .models import BuyerUser

# class BuyerUserAdmin(UserAdmin):
#     add_form = BuyerUserCreationForm
#     form = BuyerUserChangeForm
#     model = BuyerUser
#     list_display = ["email", "username",]

# admin.site.register(BuyerUser, BuyerUserAdmin)