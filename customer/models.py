from django.db import models
# from order.models import Orders
# Create your models here.


class Customers(models.Model):
    #email = models.EmailField(label='e-mail', required = True )  #changes
    email = models.EmailField(unique=True, null=True)
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    address_line3 = models.CharField(max_length=100)
    country = models.CharField(max_length=100 , default='NULL')
    City = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=30)


    # def __str__(self):
    #     return self.fname + ' ' + self.lname
