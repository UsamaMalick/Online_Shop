from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout , login
from django.urls import reverse_lazy
from django.views import generic, View
# Create your views here.
from django.views.generic import CreateView
from django.contrib.auth.models import auth
from .models import Customers
from django.contrib.auth.decorators import login_required
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
                    user = Customers.objects.create_user(first_name=first_name,
                                                         username=email,
                                                         last_name=last_name,
                                                         email=email,
                                                         password=password)
                    user.save()
                    print("Successful")
                    return render(request , 'customer/customer_info.html')
                    # try:
                    #     user = Customers.objects.create_user(first_name=first_name,
                    #                                          username=email,
                    #                                          last_name=last_name,
                    #                                          email=email,
                    #                                          password=password)
                    #     user.save()
                    #     print("Successful")
                    #     return render(request , 'customer/customer_info.html')
                    # except:
                    #     print("Something went wrong while creating account")
                    #     context = { 'message' : "Something went wrong while creating account."}
                    #     return render(request , 'customer/signUp.html' , context)
     else:
         print("Accessing First Time")
         return render(request , 'customer/signUp.html')


#this is a logout view

class LogoutView(View):
    def get(self, request,  *args, **kwargs):
        del request.session['is_login']
        logout(request)
        return redirect('/')

#handles the request for Logging in of Customer
def request_login(request):
    if request.method == 'POST':
        email = request.POST.get('id_username')
        password = request.POST.get('id_password')
        user = auth.authenticate(request, username = email, password= password)
        if user is not None:
            auth.login(request, user)
            request.session['is_login'] = 'true'
            return render(request , 'customer/customer_info.html')
        else:
            return render(request , 'customer/login_error.html')
            # return render(request, '401.html')
    else:
        login = request.session.get('is_login' , 'false')
        if  login == 'true':
            return render(request , 'customer/customer_info.html')
        return render(request , 'customer/login.html')


@login_required()
def info(request):
    return render(request , 'customer/customer_info.html')
    # try:
    #     login = request.session['is_login']
    #     if  login == True:
    #         UserEmail = request.session['email']
    #         try:
    #             UserID = Customers.objects.get(email=UserEmail)
    #         except:
    #             return render(request , 'error.html')
    #         else:
    #             OrderIDs = Orders.objects.filter(customer_id=UserID)
    #             context = { 'UserEmail' : UserEmail , 'OrderIDs' : OrderIDs }
    #             return render(request , 'customer/customer_info.html', context)
    # except KeyError:
    #     return render(request , 'customer/login_error.html')
