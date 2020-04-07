from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Products
from .models import category
from .models import Pricing
from .models import Sale
from .models import Sale_Details
from .models import Locations
from .models import product_images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' , 'slug']
    prepopulated_fields = {'slug' : ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' ,'ranking', 'product_type' , 'created_at' , 'updated_at' , 'stock' , 'available']
    list_filter = ['title' , 'product_type' , 'stock' , 'available']
    list_editable = ['stock' , 'available', 'ranking']
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(Products , ProductAdmin)
admin.site.register(category, CategoryAdmin)
admin.site.register(Pricing)
admin.site.register(Sale)
admin.site.register(Sale_Details)
admin.site.register(Locations)
admin.site.register(product_images)



