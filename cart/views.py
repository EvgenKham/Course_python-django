from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from django.views.generic.list import ListView


# from my_shop.models import MobilePhone
# from cart.models import Cart
# # from cart.form import CartAddProductForm
# # from orders.models import OrdersMobilePhone, Order
#
#
# def CartAdd(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(MobilePhone, id=product_id)
#     form = CartAddProductForm(require_POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product)