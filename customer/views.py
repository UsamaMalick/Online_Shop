from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from django.views.generic import CreateView

from .models import Customers
from order.models import Orders


def SignUp(request):
     if request.method == 'POST':
            first_name = request.POST.get('FName')
            last_name = request.POST.get('LName')
            email = request.POST.get('inputEmail')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirmPassword')

            if Customers.objects.filter(username=email).exists():
                print("Already Exist")
                context = { 'message' : "Account already Exist with this E-mail."}
                return render(request , 'customer/signUp.html' , context)
            else:
                if password == confirmPassword:
                    try:
                        user = Customers.objects.create_user(first_name=first_name,
                                                             username=email,
                                                             last_name=last_name,
                                                             email=email,
                                                             password=password)
                        user.save()
                        print("Successful")
                        return render(request , 'customer/customer_info.html')
                    except:
                        print("Something went wrong while creating account")
                        context = { 'message' : "Something went wrong while creating account."}
                        return render(request , 'customer/signUp.html' , context)
     else:
         print("Accessing First Time")
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
