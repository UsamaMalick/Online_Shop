from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from django.views.generic import CreateView

from .models import Customers
from order.models import Orders


def SignUp(request):
   return render(request , 'customer/signUp.html')

def info(request):
    try:
        login = request.session['isLoggedIn']
        if  login == True:
            UserEmail = request.session['email']
            try:
                UserID = Customers.objects.get(email=UserEmail)
            except:
                return render(request , 'error.html')
            else:
                OrderIDs = Orders.objects.filter(customer_id=UserID)
                context = { 'UserEmail' : UserEmail , 'OrderIDs' : OrderIDs }
                return render(request , 'customer/customer_info.html', context)
    except KeyError:
        return render(request , 'customer/login_error.html')
