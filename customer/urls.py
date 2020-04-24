from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    #customer/sign-up/
    path('sign-up/' , views.SignUp, name='SignUp'),
    #customer/info/
    path('info/' , views.info, name='info'),
    #customer/login/
    path('login/' , views.request_login, name='request_login'),
    #customer/logout/
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
