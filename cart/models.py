from django.db import models
from django.core.validators import RegexValidator

#zip_code_validator = RegexValidator(
 #   regex=r'^\d{5}(?:[-\s]\d{4})?$',
  #  message='Zip code must be 5 digits in format 12345 or 12345-6789',
#)
# Create your models here.
class ZipCode(models.Model):
    zipcode = models.CharField(max_length=10)
# validators=[zip_code_validator])