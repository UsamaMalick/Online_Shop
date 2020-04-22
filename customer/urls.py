from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    #customer/sign-up/
    path('sign-up/' , views.SignUp, name='SignUp'),
    #customer/info/
    path('info/' , views.info, name='info'),

]
