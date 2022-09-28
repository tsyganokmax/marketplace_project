# from liqpay import LiqPay
import liqpay
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from .cart import Cart
from .forms import CheckoutForm
from apps.order.utilities import checkout

from django.views.generic import TemplateView
from django.http import HttpResponse


def cart_detail(request):
    cart = Cart(request)
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart')
    return render(request, 'cart.html')


