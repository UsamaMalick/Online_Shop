from __future__ import unicode_literals
from django.contrib import admin

from .models import Orders
from .models import Order_Details


admin.site.register(Orders)
admin.site.register(Order_Details)

