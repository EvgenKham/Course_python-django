from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from django.views.generic.list import ListView


from my_shop.models import MobilePhone, Projector, TV
from cart.models import Cart
from cart.forms import CartAddProductForm
# from orders.models import OrderItem, Order


@require_POST
def CartAdd(request, product_id):
    """Добавить товар в корзину"""
    cart = Cart(request)
    product = get_object_or_404(MobilePhone, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:CartDetail')


def CartRemove(request, product_id):
    """Удалить товар из корзины"""
    cart = Cart(request)
    product = get_object_or_404(MobilePhone, id=product_id)

    cart.remove(product)
    return redirect('cart:CartDetail')
    pass


def CartDetail(request):
    """Просмотр корзины заказов"""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})

    return render(request, 'cart_detail.html', {'cart': cart})

