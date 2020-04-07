from audioop import reverse

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_GET

from product.models import Products, Locations, Pricing



def checkout(request):
    return render(request, 'order/checkout.html')


def remove_from_cart(request, item_slug):
    cart = request.session.get('cart', {})
    if item_slug in cart:
        cart.pop(item_slug, None)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('order:cart_detail'))
