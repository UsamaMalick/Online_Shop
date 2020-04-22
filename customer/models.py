from django.db import models
from django.contrib.auth.models import AbstractUser
# from order.models import Orders
# Create your models here.


class Customers(AbstractUser):
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    country = models.CharField(max_length=128 , null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    zip_code = models.CharField(max_length=128, null=True, blank=True)
