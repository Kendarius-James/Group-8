from django.contrib import admin
<<<<<<< Updated upstream

# Register your models here.
=======
from accounts.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
>>>>>>> Stashed changes
