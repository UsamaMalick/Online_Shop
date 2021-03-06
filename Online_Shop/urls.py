"""Online_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import  include , url

urlpatterns = [
    path('', views.home_page , name='home_page'),
    path('our-story/' , views.our_story , name='our_story'),
    path('contact/' , views.contact , name='contact'),
    path('send_email/' , views.send_email , name='send_email'),
    path('help/' , views.help , name= 'help'),
    path('admin/', admin.site.urls),

    path('order/', include('order.urls')),
    path('customer/', include('customer.urls')),
    path('product/', include('product.urls')),
    path('product/', views.product_redirect , name='product_redirect'),
]
