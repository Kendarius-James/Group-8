# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class SellerUser(AbstractUser):
    address = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField()
    company_description = models.CharField(max_length=1024, blank=True)
    phonenumber = models.CharField(max_length=10, blank=True)
    def __str__(self):
        return self.username