from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MaxValueValidator , MinValueValidator
#from django.core.urlresolvers import reverse

def self(args):
    pass

class category(models.Model):
    name = models.CharField(max_length=250 , unique=True)
    slug = models.SlugField(max_length=200 , db_index=True , unique=True)
    created_at = models.DateTimeField(default= datetime.now())

    class Meta:
        ordering = ('name' , )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    product_id = models.ForeignKey(category, on_delete=models.DO_NOTHING , default='NULL')
    title = models.CharField(max_length = 250)
    code = models.CharField(max_length=20 , default='NULL')
    slug = models.SlugField(max_length=200 , db_index=True , unique=True)
    product_type = models.CharField(max_length = 50)
    long_description = models.CharField(max_length = 500)
    short_description = models.CharField(max_length = 300)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default = 0)
    ranking = models.PositiveIntegerField(default=1 , validators=[MaxValueValidator(10) , MinValueValidator(1)])
    created_at = models.DateTimeField(default= datetime.now())
    updated_at = models.DateTimeField(default= datetime.now())
    front_image = models.ImageField(upload_to='Online_Shop/')

    class Meta:
        ordering = ('-created_at' , )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        index_together = (('id' , 'slug') , )
    def __str__(self):
        return self.title

class product_images(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    display_image = models.ImageField(upload_to='Online_Shop/')

   # def __str__(self):
       # return self. product_id

class Locations(models.Model):
    location_name=models.CharField(max_length=100)

    def __str__(self):
        return self.location_name

class Pricing(models.Model):
    product_id = models.ForeignKey(Products , on_delete=models.CASCADE)
    location = models.ForeignKey(Locations , on_delete=models.CASCADE)
    price = models.FloatField(default=models.NOT_PROVIDED)
    class Meta:
        unique_together = ('product_id', 'location')




class Sale(models.Model):
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product

class Sale_Details(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    sale_name = models.CharField(max_length=20, default='NULL', editable=True)
    sale_percentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ForeignKey(Locations, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('sale_id', 'product_id')

#
	#def__str__(self):
	# 	return self.Songtitle

