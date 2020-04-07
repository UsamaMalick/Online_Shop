from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.
from .models import Customers
from order.models import Orders


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'customer/signUp.html'

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
