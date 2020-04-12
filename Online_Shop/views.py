from django.template import loader
from django.shortcuts import render, get_object_or_404 , HttpResponseRedirect
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.signals import user_logged_in
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib import messages


from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import generic

from product.models import Products


def home_page(request):
    all_products = Products.objects.filter(available=True).order_by('-ranking' , '-created_at')

    context = { 'product' : all_products[:4] }
    return render(request , 'home.html', context)

def our_story(request):
   return render(request , 'our_story.html')

def help(request):
   return render(request , 'help.html')

def contact(request):
   return render(request , 'contact.html')



# Your email details
def send_email(request):
    FromAddr = "umalick22@gmail.com"
    PASSWORD = "ilikegmail22"

    NAME = request.GET.get('name')
    SUBJECT = request.GET.get('subject')

    EMAIL = request.GET.get('email')
    BODY = request.GET.get('message')
    ToAddr = "umalick22@gmail.com"

    MESSAGE = NAME + '\n' + SUBJECT + '\n' + BODY
    try:
        msg = MIMEMultipart()
        msg['From'] = FromAddr
        msg['To'] = ToAddr
        msg['Subject'] = EMAIL

        msg.attach(MIMEText(MESSAGE, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(FromAddr, PASSWORD)
        text = msg.as_string()
        server.sendmail(FromAddr, ToAddr, text)
        server.quit()
        messages.success(request , 'Message has Been Sent Successfully, Customer care Will contact you Soon. Thank you for Patience.')
    except:
        print("An error occurred!")
    return HttpResponseRedirect(reverse('home_page'))


def product_redirect():
    return render('product/product.html')
