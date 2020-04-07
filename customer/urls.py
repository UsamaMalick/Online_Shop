from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    #customer/signUP/
    path('sign-up/' , views.SignUp.as_view(), name='SignUp'),
    #customer/info/
    path('info/' , views.info, name='info'),

]
