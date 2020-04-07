from django.db import models

# Create your models here.
from customer.models import Customers
from product.models import Products


class Orders(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.DO_NOTHING)
    date_time = models.DateField()
    time = models.TimeField()
    class Meta:
        unique_together = ('id', 'customer_id')

class Order_Details(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product_id= models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    class Meta:
        unique_together = ('order_id', 'product_id')
